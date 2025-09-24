AI/ML Course Assignments
This repository contains my solutions and reports for the assignments in the AI/ML course. The projects cover a range of fundamental concepts in artificial intelligence and machine learning, from classical search algorithms to modern neural networks.

Assignment 1: Search Algorithms (BFS, DFS, A, Greedy Best-first)*
This assignment focused on implementing and comparing various search algorithms to solve two classic problems: the 0-1 Knapsack Problem and the Shortest Path Problem.

Key Concepts:

0-1 Knapsack Problem: A combinatorial optimization problem where the goal is to maximize the value of items in a knapsack without exceeding its weight capacity.

Breadth-first Search (BFS): A search algorithm that explores a tree or graph level by level. It is guaranteed to find the shortest path in an unweighted graph.

Depth-first Search (DFS): A search algorithm that explores as far as possible along each branch before backtracking.

Shortest Path Problem: Finding a path between two vertices in a graph such that the sum of the weights of its constituent edges is minimized.

Greedy Best-first Search: An informed search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function h(n). The objective function is f(n)=h(n).

A* Algorithm: A more optimal informed search algorithm that uses both the cost from the start node g(n) and the estimated cost to the goal h(n) to guide its search. The objective function is f(n)=g(n)+h(n).

Assignment 2: Sudoku Solver
For this assignment, I developed a solution to solve Sudoku puzzles using a state-space search approach. The project involved defining the problem in terms of AI search concepts.

Key Concepts:

State-Space Search: Representing a problem as states and transitions to find a path from an initial state to a goal state.

State Representation: How the problem's current configuration is captured (e.g., the current state of the Sudoku grid).

Initial State: The starting configuration of the problem.

Actions: The possible moves or operations that can be taken from a given state (e.g., placing a number in an empty cell).

Branching Factor (b): The number of choices available at each state.

Search Depth (m): The maximum length of any path from the initial state to a leaf node.

Assignment 3: The Traveling Salesman Problem (TSP)
This assignment focused on using metaheuristic algorithms to find an approximate solution to the Traveling Salesman Problem (TSP). I implemented and compared two different approaches.

Key Concepts:

Traveling Salesman Problem (TSP): An optimization problem that asks to find the shortest possible route that visits a set of locations exactly once and returns to the origin location.

Genetic Algorithm (GA): A metaheuristic inspired by the process of natural selection that uses mechanisms like mutation and crossover to generate high-quality solutions.

Ant Colony Optimization (ACO): A probabilistic technique for solving computational problems which can be reduced to finding paths through graphs. It is inspired by the behavior of ants finding a path from their colony to a source of food.

Assignment 4: Mancala AI (Minimax Algorithm)
In this project, I created an AI to play the ancient game of Mancala. The core of the AI's decision-making was the Minimax algorithm, which allowed the bot to plan its moves and anticipate the opponent's strategy.

Key Concepts:

Minimax Algorithm: A search algorithm used for decision making in two-player, zero-sum games. It chooses the optimal move for a player by assuming the opponent is also playing optimally.

Game Tree: A tree structure representing the possible states of a game.

Utility Function: A function that evaluates the "goodness" of a state for a player (e.g., how many stones a player has in their Mancala).

Heuristic Search: Using an evaluation function to estimate the value of a state without exploring the entire game tree.

Assignment 5: Handwritten Digit Classification (ANN)
The final assignment involved building an Artificial Neural Network (ANN) from scratch to classify handwritten digits from the famous MNIST dataset. The project demonstrated my understanding of a foundational machine learning algorithm.

Key Concepts:

MNIST Dataset: A large dataset of handwritten digits, commonly used for training image processing systems.

Artificial Neural Network (ANN): A computing system inspired by the biological neural networks that constitute animal brains.

Backpropagation: A widely used algorithm in ANNs to efficiently calculate the gradient of a loss function with respect to the weights of the network.

Hidden Layer: A layer of nodes in an ANN between the input and output layers where all the computation is done.

Accuracy: A performance metric that measures the percentage of correct predictions.

Repository Structure
Assignment1/: Code and files for the Knapsack and Shortest Path problems.

Assignment2/: Code and files for the Sudoku solver.

Assignment3/: Code and files for the TSP solutions.

Assignment4/: Code and files for the Mancala AI.

Assignment5/: Code and files for the MNIST classifier.
