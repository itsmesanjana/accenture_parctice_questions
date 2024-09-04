def decimal_binary_converstion(N):
    ans=""
    while N>0:
        if N%2==0:
            ans= "0" + ans
        else:
            ans= "1" + ans
        N=N//2
    return ans

N=int(input("Enter decimal number:"))
result=decimal_binary_converstion(N)
print("The binary representation of given decimal number is:",result)