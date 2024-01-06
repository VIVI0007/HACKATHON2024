import json
from typing import List

def parse_input(input_data):
    distances = {}
    neighborhoods = input_data.get("neighbourhoods", {})
    for n_id, n_info in neighborhoods.items():
        distances[n_id] = n_info["distances"]
    restaurants = input_data.get("restaurants",{})
    for r_id, r_info in restaurants.items():
        distances[r_id] = r_info["neighbourhood_distance"]
    return distances
def nearest_neighbor(cities: List[str], distances: dict, start) -> List[str]:
    unvisited = set(cities)
    current = start
    if current in unvisited:
        unvisited.remove(current)
    tour = [current]
    while unvisited:
        current_index = cities.index(current)
        next_city = min(unvisited, key=lambda city: distances[current_index][cities.index(city)])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    if start not in tour:
        tour.append(start)
    start_index = tour.index(start)
    tour = tour[start_index:] + tour[:start_index + 1]
    return tour

def format_output(tsp_path):
    output = {"v0": {"path": tsp_path}}
    return output



#input_file_path = "C://Users//TEMP.CS2K16//Downloads//level0.json"
#with open(input_file_path, 'r') as f:
#    input_data = json.load(f)
with open('C://Users//TEMP.CS2K16//Downloads//level0.json') as user_file:
  file_contents = user_file.read()
  
#print(file_contents)
parsed_json = json.loads(file_contents)
#print(type(parsed_json))

input_data = parsed_json

start_node = "r0"

distance_matrix = parse_input(input_data)
tsp_path = nearest_neighbor(list(distance_matrix.keys()), list(distance_matrix.values()), start_node)
output_data = format_output(tsp_path)

print(output_data)
