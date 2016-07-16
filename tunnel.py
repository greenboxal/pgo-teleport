import sys

from s2 import *
from proto.rpc_pb2  import *

from mitmproxy.models import decoded
from mitmproxy.script import concurrent

print "Pokemon Go"

delta_lat = 40.730610 - (-23.533773)
delta_lng = (-73.935242) - (-46.625290)

#10722604078531084288

request_map = {}
translation_map = {}

def patchObject(raw, typ, fn):
    obj = typ()
    obj.ParseFromString(raw)

    fn(obj)
    print(obj)

    return obj.SerializeToString()

def translateCellId(id, direction):
	old_cell = S2CellId(id)
	old_pos = old_cell.ToLatLng()

	old_lat = old_pos.lat().degrees()
	old_lng = old_pos.lng().degrees()

	new_lat = old_lat + delta_lat * direction
	new_lng = old_lng + delta_lng * direction

	print(old_lat, old_lng, new_lat, new_lng)

	new_pos = S2LatLng_FromDegrees(new_lat, new_lng)
	new_cell = S2CellId_FromLatLng(new_pos).parent(old_cell.level())

	translation_map[new_cell.id()] = id

	return new_cell.id()

def patchGetMapObjectsRequest(r):
    for i, id in enumerate(r.CellId):
        r.CellId[i] = translateCellId(id, 1)

    r.PlayerLat += delta_lat
    r.PlayerLng += delta_lng

def patchGetMapObjectsResponse(r):
    for c in r.MapCell:
        c.S2CellId = translation_map[c.S2CellId]
        
        for x in c.Fort:
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

        for x in c.FortSummary:
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

        for x in c.WildPokemon:
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

        for x in c.CatchablePokemon:
            x.Latitude -= delta_lat
            x.Longitude -= delta_lng

        for x in c.NearbyPokemon:
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
            print('<-- ' + Method.Name(p.key))

            if p.key == GET_MAP_OBJECTS:
                p.value = patchObject(p.value, GetMapObjectsProto, patchGetMapObjectsRequest)

        # Store request for future usage
        request_map[request.request_id] = request

        # Serialize new request
        flow.request.content = request.SerializeToString()

@concurrent
def response(context, flow):
    with decoded(flow.response):
        response = RpcResponseEnvelopeProto()
        response.ParseFromString(flow.response.content)

        # Patch current location
        response.lat -= delta_lat
        response.long -= delta_lng

        if response.response_id != 0:
			# Load previous request dat
			request = request_map[response.response_id]
			del request_map[response.response_id]

			for i, _ in enumerate(request.parameter):
				p = request.parameter[i]

				print('--> ' + Method.Name(p.key))

				if p.key == GET_MAP_OBJECTS:
					response.returns[i] = patchObject(response.returns[i], GetMapObjectsOutProto, patchGetMapObjectsResponse)

        # Serialize new response
        flow.response.content = response.SerializeToString()

