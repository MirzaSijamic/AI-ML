import time
import tracemalloc
"""
D=0
MW=0

with open("Assignment 1 knapsack.txt") as f:
    for line in f:
        if "DIMENSION" in line:
            for string in line.split():
                if string.isdigit():
                    D=int(string)
        if "MAXIMUM" in line:
            for string in line.split():
                if string.isdigit():
                    MW=int(string)
#print(D, MW)
"""

Max_weight=420

class Node:
    def __init__(self, level, benefit, weight, visited):
        self.level = level  # Level in the tree (item index)
        self.benefit = benefit  # Total benefit so far
        self.weight = weight  # Total weight so far
        self.visited = visited  # List of selected item IDs

    def __repr__(self):
        return "% s % s % s " % (self.level, self.benefit, self.weight)


def BFS(list_items,MaxWeight):
    #print(len(list_items))
    #print(MaxWeight)
    queue = list()
    root = Node(-1, 0, 0, [])
    queue.append(root)
    best_benefit = 0
    best_node = None
    best_taken = []

    while queue:
        current_node = queue.pop(0)
        #print(current_node)

        if int(current_node.level) >= len(list_items) - 1:
            continue

        next_level = int(current_node.level) + 1
        next_item = list_items[next_level]

        if current_node.weight + int(next_item[2]) <= MaxWeight:
            #print(next_item)
            #print(current_node.items_selected)
            #print(current_node.visited + list(next_item[0]))

            new_node = Node(next_level, current_node.benefit + int(next_item[1]), current_node.weight + int(next_item[2]), current_node.visited + [next_item[0]])
            #print(current_node.visited + list(next_item[0]))
            queue.append(new_node)

            if current_node.benefit + int(next_item[1]) > best_benefit:
                best_benefit = current_node.benefit + int(next_item[1])
                best_node = new_node
                best_taken =  current_node.visited + [next_item[0]]
                #print(best_node)

        new_node = Node(next_level, current_node.benefit, current_node.weight, current_node.visited)
        #print(current_node.visited)
        queue.append(new_node)
        #print(best_taken)

    return best_node, best_taken


def DFS(list_items,MaxWeight):
    queue = []
    root = Node(-1, 0, 0, [])
    queue.append(root)
    best_benefit = 0
    best_node = None
    best_taken = []

    while queue:
        current_node = queue.pop()

        if int(current_node.level) >= len(list_items) - 1:
            continue

        next_level = int(current_node.level) + 1
        next_item = list_items[next_level]

        if current_node.weight + int(next_item[2]) <= MaxWeight:
            new_node = Node(next_level, current_node.benefit + int(next_item[1]), current_node.weight + int(next_item[2]), current_node.visited + [next_item[0]])
            queue.append(new_node)

            if current_node.benefit + int(next_item[1]) > best_benefit:
                best_benefit = current_node.benefit + int(next_item[1])
                best_node = new_node
                best_taken =  current_node.visited + [next_item[0]]

        new_node = Node(next_level, current_node.benefit, current_node.weight, current_node.visited)
        queue.append(new_node)

    return best_node, best_taken

items_list = []
lista = []
data = open("Assignment 1 knapsack.txt", "r")
lines = data.readlines()[7:]

for line in lines:
  if "EOF" in line:
    break
  line=line.split()
  lista.append(line[0])
  lista.append(line[1])
  lista.append(line[2])
  items_list.append(lista[:])
  lista.clear()

"""
print(items_list)
for item in items_list:
    print(item)
"""
tracemalloc.start()

timeb = time.perf_counter()
print(BFS(items_list,Max_weight))

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

timea = time.perf_counter()

print("BFS memory usage: " + str(peak / (1024 * 1024))+"MB")
#print("BFS took: "+ str(timea-timeb) + "s to perform\n")


tracemalloc.start()

timeb = time.perf_counter()
print(DFS(items_list, Max_weight))

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

timea = time.perf_counter()

print("DFS memory usage: " +str(peak / (1024 * 1024))+"MB")
#print("DFS took : " + str(timea-timeb) + "s to perform\n")

#top_stats = snapshot2.compare_to(snapshot1, 'lineno')
