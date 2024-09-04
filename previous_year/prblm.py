# arr=[2,3,4,5,6,7]
# r=2
# unit=9
# total=r*unit
# sum=0

# for i in range(len(arr)):
#     sum=sum+arr[i]
#     if sum>=total:
#         print("I think its enough")
#         break
#     else:
#         print("Dont have engouh food ")


# Question

# Sure! Here’s a simplified version of the question:

# ---

# ### Problem:

# You have a group of rats, and each rat needs a certain amount of food. There are several houses, each with some food. You need to find out how many houses are needed to provide enough food for all the rats.

# ### Input:
# 1. `r`: The number of rats.
# 2. `unit`: The amount of food each rat needs.
# 3. `arr`: A list where each element represents the amount of food available in each house.

# ### Output:
# - Return the minimum number of houses needed to feed all the rats.
# - If the food in all houses combined is not enough, return `0`.
# - If the list of houses is empty or `None`, return `-1`.

# ### Example:

# #### Input:
# - `r = 7` (7 rats)
# - `unit = 2` (Each rat needs 2 units of food)
# - `arr = [2, 8, 3, 5, 7, 4, 1, 2]` (Food in each house)

# #### Output:
# - `4` (The first 4 houses provide enough food)

# #### Explanation:
# - The total food required is `7 * 2 = 14`.
# - The first 4 houses provide a total of `18` units of food, which is enough to feed all the rats.

# --- 

# This version keeps the problem straightforward and easy to understand.

def find_minimum_houses(r,unit,arr):
    if arr is None or len(arr) == 0:
        return -1
    
    total_food_required=r*unit
    food_sum=0

    for i in range(len(arr)):
        food_sum=food_sum+ arr[i]
        if food_sum>=total_food_required:
            return i
    return 0

r=int(input())
unit=int(input())
arr=list(map(int,input().split()))
#If u want to take list from user the use above statement
# input() captures the input as the string "2 8 3 5 7 4 1 2".
# .split() breaks it into ['2', '8', '3', '5', '7', '4', '1', '2'].
# map(int, ...) converts each string in the list to an integer.
# list(...) creates the final list [2, 8, 3, 5, 7, 4, 1, 2].

result=find_minimum_houses(r,unit,arr)
print(result)