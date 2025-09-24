# AI/ML Course Assignments

This repository contains my solutions and reports for the assignments in the AI/ML course.  
The projects cover a range of fundamental concepts in artificial intelligence and machine learning, from classical search algorithms to modern neural networks.

---

## Assignment 1: Search Algorithms (BFS, DFS, A\*, Greedy Best-first)

This assignment focused on implementing and comparing various search algorithms to solve two classic problems: the **0-1 Knapsack Problem** and the **Shortest Path Problem**.

### Key Concepts
- **0-1 Knapsack Problem**: A combinatorial optimization problem where the goal is to maximize the value of items in a knapsack without exceeding its weight capacity.  
- **Breadth-first Search (BFS)**: Explores a tree or graph level by level; guaranteed to find the shortest path in an unweighted graph.  
- **Depth-first Search (DFS)**: Explores as far as possible along each branch before backtracking.  
- **Shortest Path Problem**: Finding a path between two vertices such that the sum of the edge weights is minimized.  
- **Greedy Best-first Search**: Informed search algorithm that expands the node closest to the goal, using a heuristic function `h(n)`. Objective: `f(n) = h(n)`.  
- **A\***: An informed search algorithm that combines path cost `g(n)` and heuristic `h(n)`. Objective: `f(n) = g(n) + h(n)`.

---

## Assignment 2: Sudoku Solver

This project developed a solution to solve Sudoku puzzles using a **state-space search approach**.

### Key Concepts
- **State-Space Search**: Representing a problem as states and transitions to reach a goal state.  
- **State Representation**: Current configuration of the Sudoku grid.  
- **Initial State**: The starting grid configuration.  
- **Actions**: Possible moves (placing a number in an empty cell).  
- **Branching Factor (b)**: The number of choices available at each state.  
- **Search Depth (m)**: Maximum length of any path from the initial state to a leaf node.  

---

## Assignment 3: The Traveling Salesman Problem (TSP)

This assignment used **metaheuristic algorithms** to approximate solutions to the **Traveling Salesman Problem (TSP)**.

### Key Concepts
- **Traveling Salesman Problem (TSP)**: Find the shortest route visiting all locations once and returning to the start.  
- **Genetic Algorithm (GA)**: Metaheuristic inspired by natural selection; uses mutation and crossover to evolve solutions.  
- **Ant Colony Optimization (ACO)**: Probabilistic technique inspired by ants finding food paths.  

---

## Assignment 4: Mancala AI (Minimax Algorithm)

I created an AI to play **Mancala**, using the **Minimax algorithm** for decision making.

### Key Concepts
- **Minimax Algorithm**: Used in two-player, zero-sum games; chooses the optimal move assuming the opponent plays optimally.  
- **Game Tree**: Represents possible states of a game.  
- **Utility Function**: Evaluates the desirability of a state (e.g., number of stones in Mancala).  
- **Heuristic Search**: Estimates state values without exploring the entire game tree.  

---

## Assignment 5: Handwritten Digit Classification (ANN)

The final assignment built an **Artificial Neural Network (ANN)** from scratch to classify handwritten digits from the **MNIST dataset**.

### Key Concepts
- **MNIST Dataset**: Large dataset of handwritten digits, widely used for training.  
- **Artificial Neural Network (ANN)**: Computing system inspired by biological neural networks.  
- **Backpropagation**: Algorithm to compute gradients of the loss function efficiently.  
- **Hidden Layer**: Intermediate layer between input and output, performing computations.  
- **Accuracy**: Percentage of correct predictions.  

---

## Repository Structure
- `Assignment1/`: Code and files for Knapsack and Shortest Path problems  
- `Assignment2/`: Code and files for Sudoku solver  
- `Assignment3/`: Code and files for TSP solutions  
- `Assignment4/`: Code and files for Mancala AI  
- `Assignment5/`: Code and files for MNIST classifier  
