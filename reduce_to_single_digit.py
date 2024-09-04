import math
def reduce_to_single_digit(N):
    while N>=10:
        if N%2!=0:
            N=math.floor(N/2)
        else:
            N=math.floor((N-2)/2)
    return N 

# N = int(input("Enter a number (two-digit or more): "))
N=int(input("Enter the number(two-digit oor more:)"))
# # # Reducing N to a single-digit number
result = reduce_to_single_digit(N)
# # # Printing the result
print("The single-digit number is:", result)

            
    
    
    