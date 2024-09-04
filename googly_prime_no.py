#Googly_prime_no
#Ex-43=4+3=7 is prime no..

def is_prime(n):
    if n<=1:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def is_googly_prime(N):
    sum_of_digits=sum(int(digit) for digit in str(N))
    return is_prime(sum_of_digits)

N=int(input("Enter a number:"))
if is_googly_prime(N):
    print("Yes Its a googly prime..")
else:
    print("No Its not googly prime...")