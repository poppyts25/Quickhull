# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import random

# create an empty hull
hull = []

# Generate random points
test_x_1 = np.random.randint(100, size=20)
test_y_1 = np.random.randint(100, size=20)
# zip the points together to make an np array of points
points = np.array(list(zip(test_x_1, test_y_1)))

# find indexes of minimum and maximum x
min_x = min(test_x_1)
max_x = max(test_x_1)
min_index = np.where(test_x_1 == min_x)[0]
max_index = np.where(test_x_1 == max_x)[0]

# if multiple minimums, use y
temp_y = []
if min_index.size > 1:
    for i in range(0, min_index.size):
        temp_y.append(test_y_1[min_index[i]])
    min_y = min(temp_y)
    temp_index = temp_y.index(min_y)
    min_index = min_index[temp_index]
else:
    min_index = min_index[0]

# if multiple maximums, use y
temp_y = []
if max_index.size > 1:
    for i in range(0, max_index.size):
        temp_y.append(test_y_1[max_index[i]])
    max_y = min(temp_y)
    temp_index = temp_y.index(max_y)
    max_index = max_index[temp_index]
else:
    max_index = max_index[0]
    
# store points of initial line
l1, l2 = points[min_index], points[max_index]

# function to calculate the gradient and y intercept of a line between the two given points
def calculate_equation(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2:  
        return (x1, float('inf'))  
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    return c, m

# function to check if a point is above the line
def above(px, py, m, c):
    if m == float('inf'):  
        return px > c
    return py > (m * px + c)

# function to check if a point is below the line
def below(px, py, m, c):
    if m == float('inf'):  
        return px < c
    return py < (m * px + c)

# function to find the distance between the line and the point
def find_distance(px, py, m, c):
    if m == float('inf'):  
        return abs(px - c)
    return abs(-m * px + py - c) / math.sqrt(m**2 + 1)

# function to find the furthest point from the line
def find_furthest(points, l1, l2):
    c, m = calculate_equation(l1, l2)
    max_dist = -float('inf')
    furthest_point = None
    for p in points:
        dist = find_distance(p[0], p[1], m, c)
        if dist > max_dist:
            max_dist = dist
            furthest_point = p
    return furthest_point

# recursive function to calculate the hull of the points
def find_hull(points, l1, l2, hull, top_half):
    c, m = calculate_equation(l1, l2)
    points_above = []
    for p in points:
        if top_half:
            if above(p[0], p[1], m, c):
                points_above.append(p)
        else:
            if below(p[0], p[1], m, c):
                points_above.append(p)
    if not points_above:
        l2_in_hull = False
        for p in hull:
            if np.array_equal(p, l2):
                l2_in_hull = True
                break
        if not l2_in_hull:
            hull.append(l2)
        return
    furthest_point = find_furthest(points_above, l1, l2)
    find_hull(points_above, l1, furthest_point, hull, top_half)
    find_hull(points_above, furthest_point, l2, hull, top_half)

# calculate the hull for the top half and bottom half
hull.append(l1)
find_hull(points, l1, l2, hull, top_half=True) 
find_hull(points, l2, l1, hull, top_half=False) 

hull = np.array(hull)
print(hull)

# code to plot the convex hull on a map
plt.figure(figsize=(8, 6))
plt.scatter(points[:, 0], points[:, 1], color="blue", label="Points") 
# save a figure containing the inital points with no convex hull found
plt.savefig("Initial Plot")
# plot the points of the convex hull
plt.plot(
    np.append(hull[:, 0], hull[0, 0]),
    np.append(hull[:, 1], hull[0, 1]),
    color="red",
    label="Convex Hull",
) 
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Convex Hull")
plt.legend()
plt.grid(True)
# save the convex hull
plt.savefig("Convex hull")
plt.close()

# extra code to show first steps of the algorithm
plt.figure(figsize=(8, 6))
plt.scatter(points[:, 0], points[:, 1], color="blue", label="Points")  
plt.plot((l1[0],l2[0]), (l1[1],l2[1]), color="red")
plt.savefig("Line")