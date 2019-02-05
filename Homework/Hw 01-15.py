# Markus Ahling
# CSCI 136

#11.2.4
# Suppose that a and b are integers. Simplify this expression:
#(not (a < b) and not (a > b))
a == b


# 1.2.10
# Does (math.sqrt(2) * math.sqrt(2) == 2) evaluate to True or False
False
# 1.2.14
# A physics student gets unexpected results when using the code
# force = G * mass1 * mass2 / radius * radius
# to compute values according to the formula F = G m_1 m_2 / r^2. Explain the problem and correct the code.

force = G * (mass1 * mass2) / radius ** 2

# 1.2.15
# Suppose that x and y are two floats that represent the Cartesian coordinates of a point (x, y) in the plane. Give an expression that evaluates to the distance of the point from the origin.
import math

origin = float(0, 0)
cord1 = float(x, y)

distance =  float(sqrt((x ** 2) + (y ** 2))
