#Finding prime numbers upto N
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_up_to(N):
    prime_numbers = []
    for num in range(2, N + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Get user input and find primes
N = int(input("Enter a number: "))
primes = find_primes_up_to(N)
print(f"Prime numbers up to {N}: {primes}")