import requests
import xml.etree.ElementTree as ET
import geopy.distance


class Node:
    def __init__(self, _id, _coordinates, _distance):
        self.id = _id
        self.coordinates = _coordinates
        self.distance = _distance
        self.tags = {}



# non esiste un ordine vero e proprio, è random
# url = '	https://lz4.overpass-api.de/api/interpreter'
# url2 = 'https://z.overpass-api.de/api/interpreter'
# url3 = 'https://maps.mail.ru/osm/tools/overpass/api/interpreter'
url4 = 'https://overpass.kumi.systems/api/interpreter'
radius = 200
latitude = 45.97168
longitude = 8.93720
coords_1 = (latitude, longitude)
request = {'data': '(way(around:' + str(radius) + ',' + str(latitude) + ',' + str(longitude) + '););out center;'}

# response = requests.post(url, data=request)
# response2 = requests.post(url2, data=request)
# response3 = requests.post(url3, data=request)
response4 = requests.post(url4, data=request)
# print(response.elapsed.total_seconds())
# print(response2.elapsed.total_seconds())
# print(response3.elapsed.total_seconds())
print("response time " + str(response4.elapsed.total_seconds()))

nodes = []

tree = ET.fromstring(response4.content)
for child in tree.findall('way'):
    nodeId = child.attrib['id']
    print(child.tag, nodeId)
    print(child.find('center').tag + " " + str(child.find('center').attrib))
    elementLat = child.find('center').attrib['lat']
    elementLon = child.find('center').attrib['lon']
    coords_2 = (elementLat, elementLon)
    distance = geopy.distance.distance(coords_1, coords_2).meters
    print('The distance between our point and this point is: ' + str(
        distance) + ' meters')
    node = Node(nodeId, coords_2, distance)
    nodeTags = {}
    for tag in child.findall('tag'):
        tagKey = tag.attrib['k']
        tagValue = tag.attrib['v']
        nodeTags[tagKey] = tagValue
    node.tags = nodeTags
    nodes.append(node)
    print(node.tags)
    print('\n')

#sort the Nodes by ascending distance
nodes.sort(key=lambda x: x.distance)
for singleNode in nodes:
    print('Node id: '+ singleNode.id)
    print(singleNode.coordinates)
    print(singleNode.distance)
    print(singleNode.tags)
    print('\n')

print(response4.text)
