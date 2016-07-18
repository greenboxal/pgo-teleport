import sys

from s2sphere import *
from proto.rpc_pb2  import *

from expiringdict import ExpiringDict
from mitmproxy.models import decoded
from mitmproxy.script import concurrent

print "Pokemon Go"

locations = [
        (40.7829, -73.9654), # Central Park
        (-33.8688, 151.2093), # Sydney
        (37.4241, -122.1661), # Stanford
        (38.9072, -77.0369), # Washington DC
        (51.5074, -0.1278), # London
        (38.7223, -9.1393), # Lisbon
]

request_map = ExpiringDict(max_len=999999999,max_age_seconds=20)
cell_translation = ExpiringDict(max_len=999999999,max_age_seconds=20)

def get_delta_for_request(lat, lng):
    pos = LatLng.from_degrees(lat, lng)
    cell = CellId.from_lat_lng(pos).parent(10)
    id = cell.pos() >> 1
    index = id % len(locations)

    local = cell.to_lat_lng()
    local_lat = local.lat().degrees
    local_lng = local.lng().degrees

    target_lat, target_lng = locations[index]

    delta_lat = target_lat - local_lat
    delta_lng = target_lng - local_lng

    return (delta_lat, delta_lng)

def patch_coordinates(req, obj, lat_key, lng_key, direction):
    setattr(obj, lat_key, getattr(obj, lat_key) + req['delta_lat'] * direction)
    setattr(obj, lng_key, getattr(obj, lng_key) + req['delta_lng'] * direction)

def patch_object(req, raw, typ, fn):
    obj = typ()
    obj.ParseFromString(raw)

    fn(req, obj)

    return obj.SerializeToString()

def translate_cell_id(req, id, direction):
    delta_lat = req['delta_lat']
    delta_lng = req['delta_lng']

    delta = LatLng.from_degrees(delta_lat * direction, delta_lng * direction)

    old_cell = CellId(id)
    old_pos = old_cell.to_lat_lng()

    new_pos = old_pos + delta
    new_cell = CellId.from_lat_lng(new_pos)

    return new_cell

def translate_outgoing_cell_id(req, id):
    cell = translate_cell_id(req, id, 1)

    cell_translation[cell.parent(15).id()] = id

    return cell.id()

def translate_incoming_cell_id(req, id):
    return cell_translation.get(id, translate_cell_id(req, id, -1).id())

def patchWildPokemon(req, p, direction):
    patch_coordinates(req, p, 'Latitude', 'Longitude', direction)

def patchFort(req, p, direction):
    patch_coordinates(req, p, 'Latitude', 'Longitude', direction)

def patchPlayerUpdateRequest(req, r):
    patch_coordinates(req, r, 'Lat', 'Lng', 1)

def patchPlayerUpdateResponse(req, r):
    for p in r.WildPokemon:
        patchWildPokemon(req, p, -1)

    for p in r.Fort:
        patchFort(req, p, -1)

def patchGetMapObjectsRequest(req, r):
    for i, id in enumerate(r.CellId):
        r.CellId[i] = translate_outgoing_cell_id(req, id)

    patch_coordinates(req, r, 'PlayerLat', 'PlayerLng', 1)

def patchGetMapObjectsResponse(req, r):
    for i, c in enumerate(r.MapCell):
        c.S2CellId = translate_incoming_cell_id(req, c.S2CellId)

        for x in c.Fort:
            patchFort(req, x, -1)

        for x in c.FortSummary:
            patch_coordinates(req, x, 'Latitude', 'Longitude', -1)

        for x in c.WildPokemon:
            patchWildPokemon(req, x, -1)

        for x in c.CatchablePokemon:
            patch_coordinates(req, x, 'Latitude', 'Longitude', -1)

        for x in c.SpawnPoint:
            patch_coordinates(req, x, 'Latitude', 'Longitude', -1)

        for x in c.DecimatedSpawnPoint:
            patch_coordinates(req, x, 'Latitude', 'Longitude', -1)

def patchFortSearchRequest(req, r):
    patch_coordinates(req, r, 'PlayerLatDegrees', 'PlayerLngDegrees', 1)
    patch_coordinates(req, r, 'FortLatDegrees', 'FortLngDegrees', 1)

def patchGetGymDetailsRequest(req, r):
    patch_coordinates(req, r, 'PlayerLatDegrees', 'PlayerLngDegrees', 1)
    patch_coordinates(req, r, 'GymLatDegrees', 'GymLngDegrees', 1)

def patchEncounterRequest(req, r):
    patch_coordinates(req, r, 'PlayerLatDegrees', 'PlayerLngDegrees', 1)

def patchEncounterResponse(req, r):
    if r.HasField('Pokemon'):
        patchWildPokemon(req, r.Pokemon, -1)

def patchIncenseEncounterResponse(req, r):
    if r.HasField('Pokemon'):
        patchWildPokemon(req, r.Pokemon, -1)

def patchGetIncensePokemonRequest(req, r):
    patch_coordinates(req, r, 'PlayerLatDegrees', 'PlayerLngDegrees', 1)

def patchGetIncensePokemonResponse(req, r):
    patch_coordinates(req, r, 'Lat', 'Lng', -1)

def patchFortDetailsRequest(req, r):
    patch_coordinates(req, r, 'Latitude', 'Longitude', 1)

def patchFortDetailsResponse(req, r):
    patch_coordinates(req, r, 'Latitude', 'Longitude', -1)

def patchFortDeployRequest(req, r):
    patch_coordinates(req, r, 'PlayerLatDegrees', 'PlayerLngDegrees', 1)

def patchFortRecallRequest(erq, r):
    patch_coordinates(req, r, 'PlayerLatDegrees', 'PlayerLngDegrees', 1)

def patchAddFortModifierRequest(req, r):
    patch_coordinates(req, r, 'PlayerLatDegrees', 'PlayerLngDegrees', 1)

def patchTradingSearchRequest(r):
    patch_coordinates(req, r, 'Lat', 'Lng', 1)

def patchUseItemGymRequest(r):
    patch_coordinates(req, r, 'PlayerLatDegrees', 'PlayerLngDegrees', 1)

def patchDiskEncounterRequest(r):
    patch_coordinates(req, r, 'PlayerLatDegrees', 'PlayerLngDegrees', 1)

requestPatchers = {
    GET_MAP_OBJECTS: (GetMapObjectsProto, patchGetMapObjectsRequest),
    PLAYER_UPDATE: (PlayerUpdateProto, patchPlayerUpdateRequest),
    FORT_SEARCH: (FortSearchProto, patchFortSearchRequest),
    FORT_DETAILS: (FortDetailsProto, patchFortDetailsRequest),
    GET_GYM_DETAILS: (GetGymDetailsProto, patchGetGymDetailsRequest),
    #ENCOUNTER: (EncounterProto, patchEncounterRequest),
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
    INCENSE_ENCOUNTER: (IncenseEncounterOutProto, patchIncenseEncounterResponse),
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

        print('lol')

        delta_lat, delta_lng = get_delta_for_request(request.lat, request.long)

        # Create request metadata
        meta = {
            'delta_lat': delta_lat,
            'delta_lng': delta_lng
        }

        # Patch current location
        patch_coordinates(meta, request, 'lat', 'long', 1)

        print(meta, request.lat, request.long)

        for p in request.parameter:
            print('--> %s [%s]' % (Method.Name(p.key), request.request_id))

            patcher = requestPatchers.get(p.key, None)

            if patcher != None:
                typ, fn = patcher
                p.value = patch_object(meta, p.value, typ, fn)

        # Store request for future usage
        request_map[request.request_id] = (meta, request)

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
        meta, request = request_map[response.response_id]
        del request_map[response.response_id]

        for i, _ in enumerate(request.parameter):
            p = request.parameter[i]

            print('<-- %s [%s]' % (Method.Name(p.key), request.request_id))

            patcher = responsePatchers.get(p.key,  None)

            if patcher != None:
                typ, fn = patcher
                response.returns[i] = patch_object(meta, response.returns[i], typ, fn)

        # Serialize new response
        flow.response.content = response.SerializeToString()

