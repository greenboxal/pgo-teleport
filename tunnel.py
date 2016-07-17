import sys

from s2sphere import *
from proto.rpc_pb2  import *

from mitmproxy.models import decoded
from mitmproxy.script import concurrent

print "Pokemon Go"

local_lat = -23.5596626
local_lng = -46.6836279

target_lat = -35.2809
target_lng = 149.1300

delta_lat = target_lat - local_lat
delta_lng = target_lng - local_lng

request_map = {}
cell_translation = {}

def patchObject(raw, typ, fn):
    obj = typ()
    obj.ParseFromString(raw)

    fn(obj)
    print(obj)

    return obj.SerializeToString()

def translateCellId(id, direction):
    delta = LatLng.from_degrees(delta_lat * direction, delta_lng * direction)

    old_cell = CellId(id)
    old_pos = old_cell.to_lat_lng()

    new_pos = old_pos + delta
    new_cell = CellId.from_lat_lng(new_pos)

    return new_cell

def translateOutgoingCellId(id):
    cell = translateCellId(id, 1)

    cell_translation[cell.parent(15).id()] = id

    return cell.id()

def translateIncomingCellId(id):
    return cell_translation.get(id, translateCellId(id, -1).id())

def patchWildPokemon(p, direction):
    p.Latitude += delta_lat * direction
    p.Longitude += delta_lng * direction

def patchFort(p, direction):
    p.Latitude += delta_lat * direction
    p.Longitude += delta_lng * direction

def patchPlayerUpdateRequest(r):
    r.Lat += delta_lat
    r.Lng += delta_lng

def patchPlayerUpdateResponse(r):
    for p in r.WildPokemon:
        patchWildPokemon(p, -1)

    for p in r.Fort:
        patchFort(p, -1)

def patchGetMapObjectsRequest(r):
    for i, id in enumerate(r.CellId):
        r.CellId[i] = translateOutgoingCellId(id)

    r.PlayerLat += delta_lat
    r.PlayerLng += delta_lng

def patchGetMapObjectsResponse(r):
    for i, c in enumerate(r.MapCell):
        c.S2CellId = translateIncomingCellId(c.S2CellId)

        for x in c.Fort:
            patchFort(x, -1)

        for x in c.FortSummary:
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

        for x in c.WildPokemon:
            patchWildPokemon(x, -1)

        for x in c.CatchablePokemon:
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

        for x in c.SpawnPoint:
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

        for x in c.DecimatedSpawnPoint:
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

def patchFortSearchRequest(r):
    r.PlayerLatDegrees += delta_lat
    r.PlayerLngDegrees += delta_lng
    r.FortLatDegrees += delta_lat
    r.FortLngDegrees += delta_lng

def patchGetGymDetailsRequest(r):
    r.PlayerLatDegrees += delta_lat
    r.PlayerLngDegrees += delta_lng
    r.GymLatDegrees += delta_lat
    r.GymLngDegrees += delta_lng

def patchEncounterRequest(r):
    r.PlayerLatDegrees += delta_lat
    r.PlayerLngDegrees += delta_lng

def patchEncounterResponse(r):
    patchWildPokemon(r.Pokemon, -1)

def patchGetIncensePokemonRequest(r):
    r.PlayerLatDegrees += delta_lat
    r.PlayerLngDegrees += delta_lng

def patchGetIncensePokemonResponse(r):
    r.Lat -= delta_lat
    r.Lng -= delta_lng

def patchFortDetailsRequest(r):
    r.Latitude += delta_lat
    r.Longitude += delta_lng

def patchFortDetailsResponse(r):
    r.Latitude -= delta_lat
    r.Longitude -= delta_lng

def patchFortDeployRequest(r):
    r.PlayerLatDegrees += delta_lat
    r.PlayerLngDegrees += delta_lng

def patchFortRecallRequest(r):
    r.PlayerLatDegrees += delta_lat
    r.PlayerLngDegrees += delta_lng

def patchAddFortModifierRequest(r):
    r.PlayerLatDegrees += delta_lat
    r.PlayerLngDegrees += delta_lng

def patchTradingSearchRequest(r):
    r.Lat += delta_lat
    r.Lng += delta_lng

def patchUseItemGymRequest(r):
    r.PlayerLatDegrees += delta_lat
    r.PlayerLngDegrees += delta_lng

def patchDiskEncounterRequest(r):
    r.PlayerLatDegrees += delta_lat
    r.PlayerLngDegrees += delta_lng

requestPatchers = {
    GET_MAP_OBJECTS: (GetMapObjectsProto, patchGetMapObjectsRequest),
    PLAYER_UPDATE: (PlayerUpdateProto, patchPlayerUpdateRequest),
    FORT_SEARCH: (FortSearchProto, patchFortSearchRequest),
    FORT_DETAILS: (FortDetailsProto, patchFortDetailsRequest),
    GET_GYM_DETAILS: (GetGymDetailsProto, patchGetGymDetailsRequest),
    ENCOUNTER: (EncounterProto, patchEncounterRequest),
    GET_INCENSE_POKEMON: (GetIncensePokemonProto, patchGetIncensePokemonRequest),
    FORT_DEPLOY_POKEMON: (FortDeployProto, patchFortDeployRequest),
    FORT_RECALL_POKEMON: (FortRecallProto, patchFortRecallRequest),
    ADD_FORT_MODIFIER: (AddFortModifierProto, patchAddFortModifierRequest),
    TRADE_SEARCH: (TradingSearchProto, patchTradingSearchRequest),
    USE_ITEM_GYM: (UseItemGymProto, patchUseItemGymRequest),
    DISK_ENCOUNTER: (DiskEncounterProto, patchDiskEncounterRequest),
}

responsePatchers = {
    PLAYER_UPDATE: (PlayerUpdateOutProto, patchPlayerUpdateResponse),
    GET_MAP_OBJECTS: (GetMapObjectsOutProto, patchGetMapObjectsResponse),
    FORT_DETAILS: (FortDetailsOutProto, patchFortDetailsResponse),
    ENCOUNTER: (EncounterOutProto, patchEncounterResponse),
    GET_INCENSE_POKEMON: (GetIncensePokemonOutProto, patchGetIncensePokemonResponse),
    
}

@concurrent
def serverconnect(context, server_conn):
    server_conn.address = ('pgorelease.nianticlabs.com', 443)

@concurrent
def request(context, flow):
    if flow.match("~d pgorelease.nianticlabs.com"):
        request = RpcRequestEnvelopeProto()
        request.ParseFromString(flow.request.content)

        # Patch current location
        request.lat += delta_lat
        request.long += delta_lng

        for p in request.parameter:
            print('--> %s [%s]' % (Method.Name(p.key), request.request_id))

            patcher = requestPatchers.get(p.key, None)

            if patcher != None:
                typ, fn = patcher
                p.value = patchObject(p.value, typ, fn)

        # Store request for future usage
        request_map[request.request_id] = request

        # Serialize new request
        flow.request.content = request.SerializeToString()

@concurrent
def response(context, flow):
    with decoded(flow.response):
        response = RpcResponseEnvelopeProto()
        response.ParseFromString(flow.response.content)

        if response.response_id == 0:
            return

        # Load previous request dat
        request = request_map[response.response_id]
        del request_map[response.response_id]

        for i, _ in enumerate(request.parameter):
            p = request.parameter[i]

            print('<-- %s [%s]' % (Method.Name(p.key), request.request_id))

            patcher = responsePatchers.get(p.key,  None)

            if patcher != None:
                typ, fn = patcher
                response.returns[i] = patchObject(response.returns[i], typ, fn)

        # Serialize new response
        flow.response.content = response.SerializeToString()

