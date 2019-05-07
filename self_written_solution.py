import json
import numpy as np

# funktion which finds min distance value for the nodes in q and returns the index in q
def findMin(q, dist):
    minimum = float('inf')
    index = -1
    for v in q:
        tmp = dist[v]
        if tmp < minimum:
            minimum = tmp
            index = v
    
    return index

# implementation of the dijkstra alorithm (really straight forward)
def dijkstra(nodes, edges, source, target):
    q = []
    dist = np.zeros(len(nodes), dtype=float)
    prev = np.zeros(len(nodes), dtype=float)

    # initialization
    for v in nodes:         
        dist[v] = float('inf')
        prev[v] = np.nan
        q.append(v)                 
    dist[source] = 0.0                     
      
    while len(q) is not 0:
        m = findMin(q, dist)

        u = m
        q.remove(m)

        if u == target:
            break

        for e in edges:
            if e[0] == u:
                v = e[1]
                if e[1] in q:
                    alt = dist[u] + e[2]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u

    s = []
    u = int(target)
    cost = dist[u]
    if (not np.isnan(prev[u])) or (u == source):   
        while not np.isnan(u):              
            s.append(int(u))
            u = prev[int(u)]

    return s[::-1],cost

# read data
def getGraphFromJson():
    with open('generatedGraph.json') as json_file:  
        data = json.load(json_file)
    
    return data


if __name__ == "__main__":
    data = getGraphFromJson()
    nodes = []
    edges = []

    for index, n in enumerate(data['nodes']):
        nodes.append(index)

    for e in data['edges']:
        edges.append((e['source'], e['target'], e['cost']))
        edges.append((e['target'], e['source'], e['cost']))

    path = dijkstra(nodes, edges, 18, 246)

    for n in path[0]:
        print(data['nodes'][n]['label'])

    print("\nTotal cost from Erde to b3-r7-r4nd7: " + str(path[1]))