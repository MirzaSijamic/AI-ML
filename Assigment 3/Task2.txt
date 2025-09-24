import numpy as np
import random
import math


#calc Euclidean distance between two cities.
def euclidean_distance(city1, city2):
    diff_x = city1[0] - city2[0]
    diff_y = city1[1] - city2[1]
    distance = math.sqrt(diff_x * diff_x + diff_y * diff_y)
    return distance


#Ova funkcija pravi matricu distanci izmedu parova gradova
def compute_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix


# Set algorithm parameters
num_ants = 30
num_iterations = 100  #number of iterations for the algorithm
alpha = 1.0  #Pheromone
beta = 5.0  #Distance
evaporation_rate = 0.5
pheromone_constant = 100.0


def ant_colony_optimization(cities):
    num_cities = len(cities)
    distance_matrix = compute_distance_matrix(cities)
    #print(distance_matrix)

    #Initialize pheromones to 1
    pheromones = np.ones((num_cities, num_cities))

    best_route = None
    best_distance = float('inf')



    for iteration in range(num_iterations):
        #inic routes i distances empty list
        all_routes = []
        all_distances = []

        #Loop for each ant
        for ant in range(num_ants):
            current_route = [0]  #Start at the first city
            unvisited = list(range(1, num_cities))

            #Build the route for the current ant
            while len(unvisited) > 0:
                current_city = current_route[-1]
                prob_list = []

                #Calc probability for each unvisited city
                for city in unvisited:
                    pheromone = pheromones[current_city][city] ** alpha
                    visibility = (1.0 / distance_matrix[current_city][city]) ** beta
                    #print(visibility)

                    prob_value = pheromone * visibility
                    prob_list.append((city, prob_value))

                #Normalise the probabilities
                total_prob = 0.0

                for city, prob in prob_list:
                    total_prob += prob

                normalized_probs = []
                for city, prob in prob_list:
                    normalized_probs.append((city, prob / total_prob))

                #print(nomalized_probs)

                #sljed grad po prob
                rand_val = random.random()
                cumulative_prob = 0.0
                chosen_city = None

                for city, prob in normalized_probs:
                    cumulative_prob += prob
                    if rand_val <= cumulative_prob:
                        chosen_city = city
                        break


                current_route.append(chosen_city)
                unvisited.remove(chosen_city)

            # Close the loop by returning to the start city
            current_route.append(0)

            #izracunaj tot dist
            total_distance = 0.0
            for i in range(len(current_route) - 1):
                total_distance += distance_matrix[current_route[i]][current_route[i + 1]]

            all_routes.append(current_route)
            all_distances.append(total_distance)

            #Update the best route
            if total_distance < best_distance:
                best_distance = total_distance
                best_route = current_route

        #evaporate pheromones on all edges
        for i in range(num_cities):
            for j in range(num_cities):
                pheromones[i][j] = pheromones[i][j] * (1 - evaporation_rate)


        for idx in range(len(all_routes)):

            route = all_routes[idx]
            route_distance = all_distances[idx]
            #print(route)
            #print(route_distance)

            for i in range(len(route) - 1):
                deposit = pheromone_constant / route_distance
                pheromones[route[i]][route[i + 1]] += deposit
                pheromones[route[i + 1]][route[i]] += deposit

            #print(deposit)

    new_route = []
    for city in best_route:
        new_route.append(city + 1)

    return new_route, best_distance


cities = [
    [565, 575], [25, 185], [345, 750], [945, 685], [845, 655], [880, 660], [25, 230],
    [525, 1000], [580, 1175], [650, 1130], [1605, 620], [1220, 580], [1465, 200], [1530, 5],
    [845, 680], [725, 370], [145, 665], [415, 635], [510, 875], [560, 365], [300, 465],
    [520, 585], [480, 415], [835, 625], [975, 580], [1215, 245], [1320, 315], [1250, 400],
    [660, 180], [410, 250], [420, 555], [575, 665], [1150, 1160], [700, 580], [685, 595],
    [685, 610], [770, 610], [795, 645], [720, 635], [760, 650], [475, 960], [95, 260],
    [875, 920], [700, 500], [555, 815], [830, 485], [1170, 65], [830, 610], [605, 625],
    [595, 360], [1340, 725], [1740, 245]
]

best_path, best_distance = ant_colony_optimization(cities)

print("Best Route:", best_path)
print("Best Distance:", best_distance)
