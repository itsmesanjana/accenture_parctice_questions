import math

# Function to calculate the length of the hypotenuse and round it up
def calculate_hypotenuse(a, b):
    return math.ceil(math.sqrt(a**2 + b**2))

# Reading the input
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    result = calculate_hypotenuse(a, b)
    print(result)