def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def sum_at_prime_idxs(arr):
    prime_sum=0
    for i in range(len(arr)):
        if is_prime(i):
            prime_sum+=arr[i]
    return prime_sum    
    

arr=[10,20,30,40,50,60,70,80,90,100]
result=sum_at_prime_idxs(arr)
print("Sum of the values present at prime indices:",result)