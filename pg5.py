import math

def rectangle_area(length, breadth):
    return length * breadth

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)

def circle_area(radius):
    return math.pi * radius * radius

def circle_perimeter(radius):
    return 2 * math.pi * radius

def cuboid_volume(length, breadth, height):
    return length * breadth * height

def cuboid_surface_area(length, breadth, height):
    return 2 * (length * breadth + breadth * height + length * height)

def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

def sphere_surface_area(radius):
    return 4 * math.pi * radius ** 2

from __main__ import rectangle_area, rectangle_perimeter
from __main__ import circle_area, circle_perimeter
from __main__ import cuboid_volume, cuboid_surface_area
from __main__ import sphere_volume, sphere_surface_area

print("Rectangle Area:", rectangle_area(5, 3))
print("Rectangle Perimeter:", rectangle_perimeter(5, 3))

print("Circle Area:", circle_area(7))
print("Circle Perimeter:", circle_perimeter(7))

print("Cuboid Volume:", cuboid_volume(3, 4, 5))
print("Cuboid Surface Area:", cuboid_surface_area(3, 4, 5))

print("Sphere Volume:", sphere_volume(7))
print("Sphere Surface Area:", sphere_surface_area(7))

from __main__ import *

print("Rectangle Area using import *:", rectangle_area(8, 6))
print("Circle Area using import *:", circle_area(10))
print("Cuboid Volume using import *:", cuboid_volume(5, 2, 3))
print("Sphere Surface Area using import *:", sphere_surface_area(6))
