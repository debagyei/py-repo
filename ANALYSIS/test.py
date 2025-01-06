
import math
import matplotlib.pyplot as plt
 
def circle_area(radius):
    return math.pi * radius ** 2
 
radius = 5
area = circle_area(radius)
 
print(f"The area of a circle with radius {radius} is: {area:.2f}")
 
radii = [1, 2, 3, 4, 5]
areas = [circle_area(r) for r in radii]
 
plt.bar(radii, areas)
plt.xlabel('Radius')
plt.ylabel('Area')
plt.title('Area of Circles with Different Radii')
plt.show()