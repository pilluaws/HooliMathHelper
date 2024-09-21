import math

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate_sin(angle):
    return math.sin(math.radians(angle))

def calculate_cos(angle):
    return math.cos(math.radians(angle))

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
