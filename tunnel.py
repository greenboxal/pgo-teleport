import sys

from s2sphere import *
from proto.rpc_pb2  import *

from mitmproxy.models import decoded
from mitmproxy.script import concurrent

print "Pokemon Go"

local_lat = -23.5596626
local_lng = -46.6836279

target_lat = 37.4241
target_lng = -122.1661

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
    try:
        delta = LatLng.from_degrees(delta_lat * direction, delta_lng * direction)

        old_cell = CellId(id)
        old_pos = old_cell.to_lat_lng()

        new_pos = old_pos + delta
        new_cell = CellId.from_lat_lng(new_pos)

        print("%s(%s) -> %s(%s)" % (old_pos, id, new_pos, new_cell.id()))

        return new_cell.id()
    except:
        return id

def patchPlayerUpdateRequest(r):
    r.Lat += delta_lat
    r.Lng += delta_lng

cell_hack = {}

def patchGetMapObjectsRequest(r):
    for i, id in enumerate(r.CellId):
        cell_hack[i] = r.CellId[i]
        r.CellId[i] = translateCellId(id, 1)

    r.PlayerLat += delta_lat
    r.PlayerLng += delta_lng

def patchGetMapObjectsResponse(r):
    for i, c in enumerate(r.MapCell):
        c.S2CellId = cell_hack.get(i, translateCellId(c.S2CellId, -1))

        for x in c.Fort:
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

        for x in c.FortSummary:
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

        for x in c.WildPokemon:
            x.SpawnPointId = translateCellId(x.SpawnPointId, -1)
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

        for x in c.CatchablePokemon:
            x.SpawnPointId = translateCellId(x.SpawnPointId, -1)
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

        for x in c.SpawnPoint:
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

        for x in c.DecimatedSpawnPoint:
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

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

            if p.key == GET_MAP_OBJECTS:
                p.value = patchObject(p.value, GetMapObjectsProto, patchGetMapObjectsRequest)
            elif p.key == PLAYER_UPDATE:
                p.value = patchObject(p.value, PlayerUpdateProto, patchPlayerUpdateRequest)

        # Store request for future usage
        request_map[request.request_id] = request

        # Serialize new request
        flow.request.content = request.SerializeToString()

@concurrent
def response(context, flow):
    with decoded(flow.response):
        response = RpcResponseEnvelopeProto()
        response.ParseFromString(flow.response.content)

        if response.response_id != 0:
            # Load previous request dat
            request = request_map[response.response_id]
            del request_map[response.response_id]

            for i, _ in enumerate(request.parameter):
                p = request.parameter[i]

                print('<-- %s [%s]' % (Method.Name(p.key), request.request_id))

                if p.key == GET_MAP_OBJECTS:
                    response.returns[i] = patchObject(response.returns[i], GetMapObjectsOutProto, patchGetMapObjectsResponse)

        # Serialize new response
        flow.response.content = response.SerializeToString()

