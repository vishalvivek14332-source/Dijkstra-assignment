# Dijkstra's Algorithm Assignment

A simple implementation of **Dijkstra's Shortest Path Algorithm** to find the minimum distance from a source vertex to all other vertices in a weighted graph with non-negative edge weights.

## 📖 About

This project demonstrates the working of **Dijkstra's Algorithm**, one of the most widely used graph algorithms for finding the shortest path between nodes.

The algorithm repeatedly selects the unvisited vertex with the smallest known distance and updates the distances of its neighboring vertices until all shortest paths are determined.

## ✨ Features

- Finds the shortest path from a source vertex.
- Works with weighted graphs having non-negative edge weights.
- Simple and easy-to-understand implementation.
- Suitable for academic assignments and learning graph algorithms.

## 🛠️ Technologies Used

- **Language:** JavaScript

## 📂 Project Structure

```
Dijkstra-assignment/
│
├── index.js        # Main implementation
├── README.md       # Project documentation
```

> *(Update the file names if your repository contains different files.)*

## 🚀 How to Run

1. Clone the repository

```bash
git clone https://github.com/vishalvivek14332-source/Dijkstra-assignment.git
```

2. Navigate to the project directory

```bash
cd Dijkstra-assignment
```

3. Run the program

```bash
node index.js
```

## 📚 Algorithm

1. Initialize the distance to every vertex as **Infinity**.
2. Set the source vertex distance to **0**.
3. Select the unvisited vertex with the minimum distance.
4. Update the distances of all adjacent vertices.
5. Repeat until all vertices have been visited.

## ⏱️ Time Complexity

| Implementation | Time Complexity |
|---------------|-----------------|
| Array-Based | **O(V²)** |
| Priority Queue (Min Heap) | **O((V + E) log V)** |

## 📈 Space Complexity

**O(V)**

## 💡 Applications

- GPS Navigation Systems
- Network Routing
- Flight Route Planning
- Robot Path Planning
- Social Network Analysis
- Transportation Networks

## 🎯 Learning Outcomes

- Understanding graph data structures
- Implementing greedy algorithms
- Finding shortest paths in weighted graphs
- Analyzing algorithm complexity

## 👨‍💻 Author

**Vishal Vivek**

GitHub: https://github.com/vishalvivek14332-source

---

⭐ If you found this project helpful, consider giving it a star!
