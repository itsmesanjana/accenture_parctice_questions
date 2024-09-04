#If the given no is odd the print the product the product of the given digits and if it is not even then print sum of the given numbers..

def even_odd(N):
    digits=[int(d) for d in str(N)]
    
    if N%2==1:
        product=1
        for digit in digits:
          product*=digit
        return product
    else:
        return sum(digits)
    
N = int(input())
print(even_odd(N))