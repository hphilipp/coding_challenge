import json
from dijkstar import Graph, find_path

# read data
def getGraphFromJson():
    with open('generatedGraph.json') as json_file:  
        data = json.load(json_file)
    
    return data

# generates the grah
def writeGraph(data, graph):
    nodes = data['nodes']
    edges = data['edges']

    for e in edges:
        graph.add_edge(nodes[e['source']]['label'], nodes[e['target']]['label'], {'cost': e['cost']})
        graph.add_edge(nodes[e['target']]['label'], nodes[e['source']]['label'], {'cost': e['cost']})


if __name__ == "__main__":
    graph = Graph()
    data = getGraphFromJson()
    writeGraph(data, graph)

    cost_func = lambda u, v, e, prev_e: e['cost']
    path = find_path(graph, 'Erde', 'b3-r7-r4nd7', cost_func=cost_func)

    print(path.nodes[0])
    for index, e in enumerate(path.edges):
        print("|")
        print("| " + "cost: " + str(path.edges[index]['cost']))
        print("|")
        print(path.nodes[index+1])

    print("\nTotal cost from Erde to b3-r7-r4nd7: " + str(path.total_cost))