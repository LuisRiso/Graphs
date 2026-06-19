# Graphs

This repository contains class materials, laboratory exercises, algorithm implementations, study notes, and a practical project developed during the **Graphs** course at the **Federal University of Itajubá (UNIFEI)**.

The course focuses on algorithm analysis, graph theory, graph algorithms, and algorithm design techniques. The implementations were mainly developed in Python, covering graph representation, traversal algorithms, connectivity, topological sorting, shortest paths, spanning trees, network flows, and practical applications of graphs in real-world problems.

## 📚 About the Course

Graphs is a course focused on understanding how graphs can be used to model relationships, networks, paths, dependencies, flows, and complex systems.

The course combines theoretical concepts with practical implementations. It starts with algorithm complexity analysis and graph fundamentals, then progresses to graph representation, paths, cycles, connectivity, trees, matchings, breadth-first search, depth-first search, minimum spanning trees, shortest paths, network flows, and algorithm design strategies such as divide and conquer, dynamic programming, and greedy methods.

This repository documents the learning process through lecture materials, lab exercises, algorithm implementations, SIGAA activities, review notes, and a final project involving urban mobility analysis using graph-based modeling.

## 🎯 Learning Objectives

The main objectives of this repository are to:

* Understand algorithm complexity analysis.
* Apply asymptotic notation to evaluate algorithm performance.
* Represent graphs using adjacency matrices and adjacency lists.
* Understand graph concepts such as vertices, edges, paths, cycles, connectivity, and trees.
* Implement breadth-first search and depth-first search.
* Study topological sorting and graph coloring.
* Implement shortest path algorithms such as Dijkstra and Bellman-Ford.
* Study minimum spanning tree algorithms such as Prim and Kruskal.
* Understand network flow problems and maximum flow algorithms.
* Apply graph theory to practical computational problems.
* Explore algorithm design techniques such as greedy algorithms, dynamic programming, and divide and conquer.
* Use Python and NumPy to implement and test graph algorithms.

## 🧠 Topics Covered

| Module               | Topic                                                                    |
| -------------------- | ------------------------------------------------------------------------ |
| Algorithm Analysis   | Correctness, performance, asymptotic notation, and complexity analysis   |
| Graph Fundamentals   | Graph characterization, vertices, edges, paths, cycles, and connectivity |
| Graph Representation | Adjacency matrix and adjacency list representations                      |
| Graph Traversal      | Breadth-first search and depth-first search                              |
| Topological Sorting  | Kahn's algorithm and ordering in directed acyclic graphs                 |
| Graph Coloring       | Coloring concepts and graph constraints                                  |
| Shortest Paths       | Dijkstra and Bellman-Ford algorithms                                     |
| Spanning Trees       | Minimum spanning trees, Prim's algorithm, and Kruskal's algorithm        |
| Network Flows        | Flow networks and maximum flow problems                                  |
| Algorithm Design     | Divide and conquer, dynamic programming, and greedy methods              |
| Applied Project      | Urban mobility analysis using graph-based modeling                       |

## 🗂️ Repository Structure

```text
.
├── Aulas Grafos
├── Labs e Algoritmos
├── README.md
└── Trabalho Grafos
```

## 📁 Main Folders

### `Aulas Grafos`

Contains the main theoretical materials used throughout the course, including slides, notes, SIGAA activities, review files, and supporting materials for both evaluation periods.

Main topics include:

* Introduction to graphs
* Graph concepts
* Isomorphism and planarity
* Paths and connectivity
* Graph search
* Topological sorting
* Graph coloring
* Shortest paths
* Spanning trees
* Network flows

### `Labs e Algoritmos`

Contains practical laboratory exercises and Python implementations of graph algorithms.

The labs are organized as follows:

| Lab    | Topic                                         |
| ------ | --------------------------------------------- |
| Lab 01 | Python basics                                 |
| Lab 02 | Graph representation using adjacency matrices |
| Lab 03 | Graph representation using adjacency lists    |
| Lab 04 | Paths and connectivity                        |
| Lab 05 | Breadth-first search                          |
| Lab 06 | Depth-first search                            |
| Lab 07 | Topological sorting                           |
| Lab 08 | Shortest path algorithms                      |
| Lab 09 | Spanning tree algorithms                      |
| Lab 10 | Maximum flow networks                         |

### `Trabalho Grafos`

Contains the final graph project, including article material, dataset files, and the project repository.

The project explores graph-based urban mobility analysis using a dataset related to Brasília. It includes network files, edge information, documentation, and an applied repository named `Urban-Mobility`.

## 🛠️ Technologies Used

* Python
* NumPy
* Graph theory
* Algorithm analysis
* Git and GitHub
* Visual Studio Code
* Linux terminal / command-line environment

## ▶️ How to Run the Python Files

To run a Python file, navigate to the desired folder and execute:

```bash
python3 filename.py
```

Example:

```bash
python3 Exercicio01.py
```

Depending on your system configuration, the command may also be:

```bash
python filename.py
```

Some exercises may depend on input files, datasets, or local files located in the same folder. In those cases, keep the required files in the expected directory before running the script.

## 📦 Dependencies

Some implementations use NumPy. To install it, run:

```bash
pip install numpy
```

A recommended approach is to create a virtual environment before installing dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy
```

If a `requirements.txt` file is created, dependencies can be installed with:

```bash
pip install -r requirements.txt
```

## 🧩 Example Concepts Practiced

Some of the concepts practiced in this repository include:

* Algorithm complexity
* Asymptotic analysis
* Graph representation with matrices
* Graph representation with adjacency lists
* Paths and cycles
* Connectivity
* Breadth-first search
* Depth-first search
* Topological sorting
* Kahn's algorithm
* Graph coloring
* Dijkstra's algorithm
* Bellman-Ford algorithm
* Prim's algorithm
* Kruskal's algorithm
* Minimum spanning trees
* Maximum flow networks
* Flow representation using matrices and adjacency lists
* Applied graph modeling
* Urban mobility network analysis

## 🌐 Graph Theory Concepts

Graph theory is a mathematical and computational framework used to represent relationships between objects.

In this repository, graphs are used to model structures such as:

* Networks
* Routes
* Dependencies
* Connections
* Flows
* Urban mobility systems

The main graph concepts explored include:

* **Vertices and edges:** basic graph components.
* **Paths and cycles:** sequences of connected vertices.
* **Connectivity:** whether vertices or components are reachable from one another.
* **Trees:** connected acyclic structures.
* **Graph traversal:** systematic exploration of vertices and edges.
* **Shortest paths:** finding minimum-cost routes between vertices.
* **Spanning trees:** connecting all vertices with minimum total cost.
* **Network flows:** modeling capacity and flow between sources and destinations.

## 🏙️ Final Project

The final project applies graph theory to an urban mobility context.

The project folder includes:

* An academic article/report
* Brasília graph dataset files
* Edge information
* Network representation files
* A project repository named `Urban-Mobility`

The goal is to explore how graphs can support the analysis of urban structures, connectivity, and mobility-related relationships.

## 📌 Notes

This repository is intended for academic study and personal learning documentation. Some folders contain theoretical materials, while others contain practical algorithm implementations and applied graph projects.

The main source files are the `.py` files. Dependency folders such as `numpy`, `numpy.libs`, and `bin` should not be versioned, since they can be recreated using a virtual environment and package installation.

## 👨‍💻 Author

Developed by **Luis Gustavo Riso** as part of the Graphs course at UNIFEI.

GitHub: [LuisRiso](https://github.com/LuisRiso)
