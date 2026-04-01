# Optimal Route Finder with Dynamic Cost Analysis
* This project is a Python-based pathfinding application designed to find the least expensive route through a grid-based map. It utilizes a backtracking algorithm to navigate from the leftmost column to the rightmost column while calculating costs dynamically based on proximity to obstacles (sinkholes).


## ✨ Features
* Dynamic Cost Calculation: Costs are not static; they are determined by the cell's surroundings.

* Proximity to Sinkholes: Higher costs are applied if a cell is adjacent or diagonal to a "sinkhole" (represented by 0).

* Optimized Pathfinding: Uses a recursive backtracking approach to explore all possible routes and identify the one with the minimum total cost.

* Intelligent Movement: The algorithm prioritizes movements (Right, Up, Down, Left) to find the most efficient path through available cells (represented by 1).

* Obstacle Awareness: Successfully navigates around sinkholes and non-traversable areas while accounting for "visited" cells to prevent infinite loops.

* Visualized Output: Generates an output map where the optimal path is marked with X, making it easy to visualize the final result.


## 🚀 Usage
* The program takes an input file containing cost values and the map, and produces an output file with the results.
```python3 route_finder.py input.txt output.txt```


## 📊 Logic & Methodology
* The core of this project lies in its Recursive Backtracking function:

* It explores every possible path from every starting point in the first column.

* It calculates the cumulative cost as it moves.

* If a new path is found with a lower cost than the current minimum, the system updates the "best route."

## 🛠️ Technologies Used
* Language: Python 3.x

* Modules: sys (for command-line argument handling)

Algorithms: Recursive Backtracking, Dynamic Cost Analysis, Grid Traversal.


📝 Project Context
Developed to demonstrate proficiency in algorithm design, specifically focusing on optimization problems and spatial data processing.
