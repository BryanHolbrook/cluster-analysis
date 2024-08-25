# Cluster Analysis
A program that analyzes clusters of 1's in binary text files in a regular N x M sized grid.

Summary
* Functionality: The code reads a grid from a file, where the grid is composed of '1's and '0's. It then counts how many connected shapes (clusters of '1's) exist in the grid using (DFS) Depth-First Search on the grid starting from a specific cell (x, y) to explore and mark all connected '1's (representing part of the same shape). The program then counts the number of connected shapes (groups of connected '1's) in the grid and then displays the number of clusters (connected '1's) in the print statement.

* Usage: This could be used for problems like counting islands in a 2D grid, connected components in graphs, or any scenario where you need to identify and count clusters in a matrix.
