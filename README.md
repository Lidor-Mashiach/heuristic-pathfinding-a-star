# 🤖 Heuristic Pathfinding with A* (Grid-Based Robot Navigation)

This project implements an intelligent robot navigating a 2D grid world using the **A\*** search algorithm.  
The robot must find an optimal path to a glowing target (the lamp) while avoiding obstacles and elevation constraints.

Two heuristic strategies are compared to evaluate search efficiency and accuracy:

- 🧠 **Naive Heuristic** – Straight-line (Manhattan) distance to the goal.
- 🚀 **Advanced Heuristic** – Considers movement cost, elevation differences, and tile structure.

The project was developed in an academic setting to demonstrate heuristic search design, state-space modeling, and informed decision-making in constrained environments.

---
## 📁 Project Structure & Key Components

The codebase is modular and organized for clarity and extensibility:

- `main.py`  
  Launches the search simulation.  
  Defines the initial map, goal location, and executes the A* search with both heuristics.

- `search.py`  
  Core implementation of the A* algorithm.  
  Supports pluggable heuristics and outputs the optimal path and search statistics.

- `search_node.py`  
  Defines a node in the search tree.  
  Tracks parent-child relationships, cost-to-reach (`g`), heuristic estimate (`h`), and total cost (`f = g + h`).

- `grid_robot_state.py`  
  Models the grid-based robot environment.  
  Encodes the map, current location, allowed movements, and state transitions.

- `heuristics.py`  
  Contains two heuristic functions:
  - `naive_heuristic`: Returns the Manhattan distance.
  - `advanced_heuristic`: Considers tile elevation and movement constraints.

Each module is documented with inline explanations for learning and extension purposes.

---
## 🔄 How It Works – A* Algorithm Overview

The project simulates an A* search through a robot’s navigation grid, aiming to find the most efficient path to a goal location using different heuristics.

1. **Initialization**
   - The grid is defined with obstacles, allowed movement directions, and elevation values.
   - The initial and goal locations are set.
   - The search begins from the robot’s starting point.

2. **Search Execution**
   - A* is executed using either a **naive heuristic** (Manhattan distance) or a more **advanced heuristic** that incorporates terrain cost.
   - At each iteration, the algorithm:
     - Selects the node with the lowest estimated total cost `f = g + h`.
     - Expands possible movements (up, down, left, right) while considering map boundaries and obstacles.
     - Tracks visited states and reconstructs the optimal path once the goal is reached.

3. **Efficiency Optimization**
   - To reduce memory overhead and runtime, the algorithm avoids storing full grid states.
   - Instead, it keeps **only the essential metadata** required to reconstruct the path and evaluate neighbor states.
   - This design significantly improves performance in larger grids and sparse search spaces.

4. **Result Reporting**
   - Once the goal is found, the program prints:
     - Total cost
     - Number of nodes visited
     - Time taken
     - Optimal path from start to goal

This modular framework enables easy replacement or comparison of heuristics, making it useful for academic or research settings in **robotics**, **AI pathfinding**, or **search optimization**.

---
## ▶️ How to Run

> 🧪 This project was designed for academic experimentation and can be executed from the command line.

1. Make sure all project files are in the same directory:
   - `main.py`
   - `search.py`
   - `search_node.py`
   - `grid_robot_state.py`
   - `heuristics.py`

2. Run the main script:
```bash
  python main.py
```
3. You’ll be prompted to choose:
   - A predefined board (e.g., with blocked cells and custom robot/goal positions)
   - Or define your own board dimensions and positions

The script will then:
- Print the resulting path from start to goal
- Show path length, number of expanded nodes, and execution time
