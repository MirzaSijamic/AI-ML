import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Set backend before importing pyplot
import matplotlib.pyplot as plt

# ... [rest of your code, including locations, distance, etc.] ...

def genetic_algorithm():
    pop_size = 50  # Reduced for faster execution
    generations = 100  # Reduced for faster execution
    population = init_population(pop_size)
    best_route = population[0]
    best_distance = route_distance(best_route)
    performance_history = []

    for gen in range(generations):
        new_population = []
        for _ in range(pop_size // 2):
            p1 = select(population)
            p2 = select(population)
            child1 = crossover(p1, p2)
            child2 = crossover(p2, p1)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        population = new_population

        current_best = min(population, key=lambda x: route_distance(x))
        current_best_dist = route_distance(current_best)
        if current_best_dist < best_distance:
            best_route = current_best
            best_distance = current_best_dist
        performance_history.append(best_distance)

        # Progress tracking
        if gen % 10 == 0:
            print(f"Generation {gen}: Best Distance = {best_distance}")

    return [1] + best_route + [1], best_distance, performance_history

try:
    best_route, best_distance, performance_history = genetic_algorithm()
    print("\nFinal Best Route:", best_route)
    print("Final Shortest Distance:", best_distance)

    plt.plot(performance_history)
    plt.xlabel('Generation')
    plt.ylabel('Best Distance')
    plt.title('Evolution of Best Distance over Generations')
    plt.grid(True)
    plt.show()
except Exception as e:
    print(f"Error during execution: {e}")