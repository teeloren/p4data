# Write a function that takes in 2 points (2 tuples) on a coordinate axes, so
# (x, y). This function should then return the distance between them. Hint:
# Think of the pythagorean theorem a^2 + b^2 = c^2.
# Write a function that takes in 2 points (2 tuples)

# full breakdown
#import math
# def distancetup(x, y):
#     x = (x[0], x[1])  # 2 points(2 tuples) on a coordinate axes, (x, y)
#     y = (y[0], y[1])

#     # This function should then return the distance between them.
#     a = (x[0]-x[1])**2 + (y[0]-y[1])**2
#     print(a)
#     distance = math.sqrt(a)  # Distance Formula
#     return distance
# t=(5, 3)
# p=(4,5)
# distancetup(t,p)

import math


def distance(x, y):
    x = (x[0], x[1])
    y = (y[0], y[1])
    return math.sqrt((x[1]-x[0])**2 + (y[1]-y[0])**2)


distance((5, 3), (4, 5))
