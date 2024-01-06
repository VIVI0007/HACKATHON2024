import json
from typing import List
from pathlib import Path
from typing import List, Dict


def parse_input(input_data):
    distances = {}
    neighborhoods = input_data.get("neighbourhoods", {})
    restaurants = input_data.get("restaurants", {})
    
    for entity_id, entity_info in {**neighborhoods, **restaurants}.items():
        distances[entity_id] = entity_info.get("distances", entity_info.get("neighbourhood_distance", []))

    return distances

def nearest_neighbor(cities: List[str], distances: dict, start, visited) -> List[str]:
    unvisited = set(cities) - set(visited)
    current = start
    if current in unvisited:
        unvisited.remove(current)
    tour = [current]

    while unvisited:
        current_index = cities.index(current)
        next_city = min(unvisited, key=lambda city: distances[current][cities.index(city)])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    if start not in tour:
        tour.append(start)

    start_index = tour.index(start)
    tour = tour[start_index:] + tour[:start_index + 1]
    return tour


def assign_delivery_slots(orders: Dict[str, int], scooter_capacity: int, distance_matrix: dict, start_node: str) -> Dict[str, List[str]]:
    unassigned_orders = list(orders.keys())
    delivery_slots = {}

    path_number = 1
    visited_neighborhoods = {start_node}
    while unassigned_orders:
        current_capacity = 0
        current_slot = [start_node]

        for order in unassigned_orders:
            order_quantity = orders[order]
            if order_quantity == 'INF':
                order_quantity = float('inf')
            else:
                order_quantity = int(order_quantity)

            if current_capacity + order_quantity <= float(scooter_capacity):
                current_capacity += order_quantity
                current_slot.append(order)
                visited_neighborhoods.add(order)
                unassigned_orders.remove(order)

        current_slot += nearest_neighbor(current_slot, distance_matrix, start_node, visited_neighborhoods)
        delivery_slots[f"path{path_number}"] = current_slot
        path_number += 1

        # Remove the last 'r0' from the path if it exists
        if current_slot[-1] == 'r0':
            current_slot.pop()


    return delivery_slots

def format_output(delivery_slots):
    output = {"v0": delivery_slots}
    return output

input_file_path = Path("C:/Users/TEMP.CS2K16/Downloads/level0.json")

with input_file_path.open('r') as f:
    input_data = json.load(f)

#start_node = "r0"
start_node = input_data["vehicles"]["v0"]["start_point"]
scooter_capacity = input_data["vehicles"]["v0"]["capacity"]

distance_matrix = parse_input(input_data)

# Extracting order quantities from the neighborhoods
orders = {neighborhood: data["order_quantity"] for neighborhood, data in input_data["neighbourhoods"].items()}


# ... (rest of the code remains the same)

delivery_slots = assign_delivery_slots(orders, scooter_capacity, distance_matrix, start_node)
print(delivery_slots)
output_data = format_output(delivery_slots)



#distance_matrix = parse_input(input_data)
#tsp_path = nearest_neighbor(list(distance_matrix.keys()), distance_matrix, start_node)
#output_data = format_output(tsp_path)

output_file_path = Path("level1a_output.json")

# Write output data to JSON file
with output_file_path.open('w') as output_file:
    json.dump(output_data, output_file)

print(f"Output written to {output_file_path}")
