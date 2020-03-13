graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2
graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7
graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3
graph["d"] = {}
graph["d"]["fin"] = 1
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None

processed = []

def dijkstra(graph,costs,parents,processed):
    node = find_lowest_cost_node(costs,processed)
    while node is not None:   # if you've processed all the nodes, this while loop is done.
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():  # Go through all the neighbors of this node.
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs,processed)
    print("costs=",costs["fin"])
    print("fin")
    p = parents["fin"]
    while True:
        print(p)
        p = parents[p]
        if p == "start":
            print(p)
            break


def find_lowest_cost_node(costs,processed):
    lowest_code = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_code and node not in processed:
            lowest_cost_node = node
    return lowest_cost_node
