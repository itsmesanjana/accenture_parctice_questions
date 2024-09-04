import math
def count_permutaion(s):
    vowels="aeiouAEIOU"
    count=0
    for char in s:
        if char not in vowels:
            count+=1
    return math.factorial(count)

s="abcde"
print(count_permutaion(s))     