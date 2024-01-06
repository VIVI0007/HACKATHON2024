
import numpy as np
import json
with open('C://Users//TEMP.CS2K16//Downloads//level0.json') as user_file:
  file_contents = user_file.read()
  
#print(file_contents)
parsed_json = json.loads(file_contents)
#print(type(parsed_json))

json_data = parsed_json

#for key, value in parsed_json.iteritems():
#    if key=="n_neighbourhoods":
#        print(key, ":", value)

print(my_dict['vehicles']['v0']['start_point'])     #prints r0


from sys import maxsize
from itertools import permutations

V = int(my_dict['n_neighbourhoods']) + int(my_dict['n_restaurants'])

# implementation of traveling Salesman Problem
def shortestpath(graph, s):

    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    path = []

    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0
        current_path = [s]

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            current_path.append(j)
            k = j
        current_pathweight += graph[k][s]
        current_path.append(s)

        # update minimum
        if current_pathweight < min_path:
            min_path = current_pathweight
            path = current_path

    print("Minimum Weight Hamiltonian Cycle:", path)
    return min_path

s=0
graph=[]
for neighborhood, details in my_dict["restaurants"].items():
    graph.extend(details["neighbourhood_distance"])
for neighborhood, details in my_dict["neighbourhoods"].items():
    all_distances = []
    all_distances.extend(details["distances"])
    graph.append(all_distances)
min_weight = shortestpath(graph, s)
print("Minimum Weight:", min_weight)



