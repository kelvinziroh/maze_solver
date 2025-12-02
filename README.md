# 🌀 Maze Solver
![](/images/RehzDga.gif)

A visual maze generator and solver built with **Python** and **Tkinter**.
It creates a grid, carves out a labyrinth by randomly breaking cell walls, and then animates a **Depth-First Search (DFS)** algorithm finding its way from start to finish.

## 🛠️ Tech Stack

* **Python 3.x**
* **Tkinter** (standard library)

## ▶️ How to Run

1. Clone the repo:

   ```bash
   git clone <your-repo-url>
   ```

2. Enter the project folder:

   ```bash
   cd maze_solver
   ```

3. Run the app:

   ```bash
   python3 main.py
   ```

## 🔍 How It Works (Short Version)

### 1. **Grid Creation**

A matrix of `Cell` objects is generated, each with four walls.

### 2. **Maze Carving**

A randomized DFS-style backtracking algorithm removes walls between cells, creating a perfect maze with no loops.

### 3. **Maze Solving**

Another DFS routine explores the maze, marking visited cells until it reaches the goal.

All movements are animated in the Tkinter canvas.


## 🎯 Future Improvements

* Path smoothing / shortest-path finding
* Alternative algorithms (A*, BFS, Prim’s, Kruskal’s)
* User-controlled grid size & animation speed
* Export maze as an image or JSON
