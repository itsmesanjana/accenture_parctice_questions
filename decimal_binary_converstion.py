# def decimal_binary_converstion(N):
#     ans=""
#     sum_of_bits=0
#     while N>0:
#         if N%2==0:
#             ans= "0" + ans
#         else:
#             ans= "1" + ans
#             sum_of_bits+=1
#         N=N//2
#     return ans,sum_of_bits


# N=int(input("Enter decimal number:"))
# binary_representation,sum_of_bits=decimal_binary_converstion(N)
# result=decimal_binary_converstion(N)
# print("The binary representation of given decimal number is:",binary_representation)
# print("The sum of bits in binary representation is:",sum_of_bits)

# def decimal_binary_conversion(N):
#     binary_rep = bin(N)[2:]  # bin() returns a string prefixed with '0b'
#     sum_of_bits = binary_rep.count('1')  # Count the number of '1's
#     return binary_rep, sum_of_bits

# N = int(input("Enter decimal number: "))
# binary_representation, sum_of_bits = decimal_binary_conversion(N)
# print("The binary representation of the given decimal number is:", binary_representation)
# print("The sum of bits (number of 1's) in the binary representation is:", sum_of_bits)


def decimal_binary_conversion(N):
    ans=""
    sum_of_bits=0
    
    while N>0:
        if N%2==0:
            ans="0"+ans
        else:
            ans="1"+ans
            sum_of_bits+=1
        N=N//2
    return ans,sum_of_bits

N = int(input("Enter decimal number: "))
binary_representation, sum_of_bits = decimal_binary_conversion(N)
print("The binary representation of the given decimal number is:", binary_representation)
print("The sum of bits (number of 1's) in the binary representation is:", sum_of_bits)

