def make_graph():
    graph = {}

    with open('Assignment 1 Spain map.txt', 'r') as data:
        lines = data.readlines()[5:82]

    for line in lines:
        parts = line.split()
        """
        if len(parts) < 3:
            continue
        """

        city1, city2, cost_str = parts[0], parts[1], parts[2]

        cost = int(cost_str)
        if city1 not in graph:
            graph[city1] = []

        graph[city1].append([city2, cost])
        #print(graph[city1])

        if city2 not in graph:
            graph[city2] = []
        graph[city2].append([city1, cost])
    #print(graph)
    return graph


def sld():

    heuristic_table = dict()
    with open('Assignment 1 Spain map.txt', 'r') as data:
        lines = data.readlines()[85:134]

    for line in lines:
        parts = line.split()

        city, dist_str = parts[0], parts[1]
        heuristic_table[city] = int(dist_str)
        #print(heuristic_table[city])
        #print(city)
        #print(dist_str)

    #print(heuristic_table)
    return heuristic_table





def pop_min(queue):
    best_index = 0
    #print(queue[0][2])
    best_val = queue[0][2]

    for i in range(1, len(queue)):
        if queue[i][2] < best_val:
            #print(queue[i][2])

            best_val = queue[i][2]
            best_index = i

    return queue.pop(best_index)


def gbf(start, end, graph, heuristic_table):
    current_node = [start, None, heuristic_table[start], 0]
    queue = [current_node]

    while queue:
        current_node = pop_min(queue)
        #print(current_node)
        if current_node[0] == end:
            return current_node
        children = graph.get(current_node[0], [])
        #print(children)


        for child in children:
            new_node = [child[0], current_node, heuristic_table[child[0]], current_node[3] + child[1]]
            queue.append(new_node)

    return None


def a_star(start, end, graph, heuristic_table):
    current_node = [start, None, heuristic_table[start], 0]
    queue = [current_node]

    while queue:
        current_node = pop_min(queue)
        if current_node[0] == end:
            return current_node

        children = graph.get(current_node[0], [])


        for child in children:
            #beacause there was so e confusion about the way I explained my code in code defense I will put some guidlines here as comments 
            #child[0] is ID of child node
            #current_node will be the node from which we reach this child
            #current_node[3] + child[1] is g(n)
            #euristic_table[child[0]] is h(n) 
            #f(n) = g(n) + h(n)
            #current_node[3] + child[1] is actual cost from the starting node to this child
            queue.append([child[0], current_node, current_node[3] + child[1] + heuristic_table[child[0]], current_node[3] + child[1]])

    return None


def travel_path(end_node):
    path = []
    node = end_node
    cost = end_node[3]

    while node is not None:
        path.append(node[0])
        node = node[1]

    path.reverse()

    return cost, path


graph = make_graph()
heuristic_table = sld()

print("GBF:")
result_gbf = gbf("Malaga", "Valladolid", graph, heuristic_table)

if result_gbf is not None:
    cost, path = travel_path(result_gbf)
    print("Path found:", " > ".join(path))
    print("Total cost:", cost)


print("\nA*:")
result_astar = a_star("Malaga", "Valladolid", graph, heuristic_table)

if result_astar is not None:
    cost, path = travel_path(result_astar)
    print("Optimal path:", " > ".join(path))
    print("Total cost:", cost)
