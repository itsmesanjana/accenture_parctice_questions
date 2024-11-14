def is_prime(n):
    return n>1 and all(n%i for i in range(2,int(n**0.5)+1))

def next_prime(n):
    candidate=n+1
    while not is_prime(candidate):
        candidate+=1
    return candidate

def is_next_prime(prime1,prime2):
    return is_prime(prime1) and next_prime(prime1)==prime2

num1,num2=map(int,input("Enter two numbers:").split())
print("True" if is_next_prime(num1,num2) else "False")
        