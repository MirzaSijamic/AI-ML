import random
import numpy as np

locations = [
    (565, 575), (25, 185), (345, 750), (945, 685), (845, 655), (880, 660), (25, 230),
    (525, 1000), (580, 1175), (650, 1130), (1605, 620), (1220, 580), (1465, 200), (1530, 5),
    (845, 680), (725, 370), (145, 665), (415, 635), (510, 875), (560, 365), (300, 465),
    (520, 585), (480, 415), (835, 625), (975, 580), (1215, 245), (1320, 315), (1250, 400),
    (660, 180), (410, 250), (420, 555), (575, 665), (1150, 1160), (700, 580), (685, 595),
    (685, 610), (770, 610), (795, 645), (720, 635), (760, 650), (475, 960), (95, 260),
    (875, 920), (700, 500), (555, 815), (830, 485), (1170, 65), (830, 610), (605, 625),
    (595, 360), (1340, 725), (1740, 245)
]

#Euclidian between 2 cities
def distance(p1, p2):
    d = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    return np.sqrt(d)



def route_distance(route):
    total_dist = 0
    #calc total dist of the route
    #objasni da ne dodajemo pocetak i kraj nego na kraju tek
    for i in range(len(route) - 1):
        total_dist += distance(locations[route[i]-1], locations[route[i+1]-1])
        #print(locations[route[i]-1])
    return total_dist

def nearest_neighbor_route():
    #heuristika, najbliz  neighbour
    num_cities = len(locations)
    unvisited = list(range(2, num_cities + 1)) #list of unvisited cities but no first city
    route = []
    current = 1
    #loop untill all cities are visited
    while len(unvisited) > 0:
        min_dist = float('inf')
        next_city = -1
        for city in unvisited:
            dist = distance(locations[current - 1], locations[city - 1])
            #calc dist and chech if < than min_dist
            if dist < min_dist:
                min_dist = dist
                #update the minimum distance and next city
                next_city = city
        route.append(next_city)
        #print(route)
        unvisited.remove(next_city)
        current = next_city
    return route

#oca ti funkcija generira inicijalnu populaciju
def init_population(size):
    population = []
    for i in range(size):
        if i == 0:
            #first individual is made with NNH func
            population.append(nearest_neighbor_route())
        else:
            #other are random routes
            route = list(range(2, len(locations) + 1))
            random.shuffle(route)
            population.append(route)
    #print(population)
    return population

def fitness(route):
    return 1.0 / route_distance(route) #higger the score = shorter the rout

def select(population):
    #chose the 5 random individuals from population and loop tghrouh them to find the shortest route
    candidates = []
    for i in range(5):
        candidates.append(random.choice(population))
    best = candidates[0] #predpostavljamo da je prvi najbokji
    for c in candidates:
        if route_distance(c) < route_distance(best):
            best = c
            #print(best)
    return best

def crossover(parent1, parent2):
    size = len(parent1)
    child = [-1] * size
    #random crossover points cx1 and 2
    cxpoint1 = random.randint(0, size-1)
    cxpoint2 = random.randint(cxpoint1, size-1)
    for i in range(cxpoint1, cxpoint2):
        child[i] = parent1[i]
    #for each position in the child that is still -1 I fill with a gene from parent2
    for i in range(size):
        if child[i] == -1:
            for j in range(size):
                #print(parent2[i])
                #print(child[i])
                if parent2[j] not in child:
                    child[i] = parent2[j]
                    break
    return child

def mutate(route):
    if random.random() < 0.02:
        i = random.randint(0, len(route)-1)
        j = random.randint(0, len(route)-1)
        temp = route[i]
        route[i] = route[j]
        route[j] = temp
    return route

def genetic_algorithm():
    pop_size = 200
    generations = 5000

    #inicijaliziraj populaciju
    population = init_population(pop_size)

    #najbolji je prvi i izracujanj distancu
    best_route = population[0]
    best_distance = route_distance(best_route)


    for gen in range(generations):
        new_population = []
        for notimportant in range(pop_size // 2):
            #this part creats individuals with crossover and mutation
            p1 = select(population)
            p2 = select(population)

            child1 = crossover(p1, p2)
            child2 = crossover(p2, p1)

            new_population.append(mutate(child1))
            new_population.append(mutate(child2))

        #print(new_population)
        population = new_population

        for r in population:
            if route_distance(r) < best_distance:
                best_route = r
                best_distance = route_distance(r) #update best dist
        if best_distance < 9000:
            break
    return [1] + best_route + [1], best_distance #Ovo je dio gdje se dodaje city 1 na pocetak i kraj, to objasni

#main
best_route, best_distance = genetic_algorithm()
print("Best Route:", best_route)
print("Shortest Distance:", best_distance)
