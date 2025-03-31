# Quickhull
A basic implementation of the Quickhull algorithm in Python. 

It generates a set of random points, calculates the convex hull using the Quickhull algorithm, and visualizes the result with matplotlib. The convex hull is the smallest convex polygon that encloses all the given points.

## Features
- Random Point Generation: Creates a random set of (x, y) coordinates within a 100x100 grid.
- Convex Hull Calculation: Uses the Quickhull algorithm:
  - Selects the leftmost and rightmost points.
  - Recursively finds the furthest points and splits the space.
- Visualization:
  - Plots the initial point cloud.
  - Draws the convex hull outline in red.
  - Saves the initial and final visualizations as image files.
- Distance and Line Classification:
  - Calculates the perpendicular distance from a point to a line.
  - Classifies points as above or below the current hull line.

## Technologies Used
- Python
- Libraries:
  - numpy → For numerical operations and point manipulation.
  - matplotlib → For plotting the points and hull.
