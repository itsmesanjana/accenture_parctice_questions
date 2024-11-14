# add a=2,b=3 without using + operator.

def get_sum(a,b):
    Max=0x7FFFFFFF
    Mask=0xFFFFFFF
    
    while b!=0:
        xor_sum=(a^b)&Mask
        carry=((a&b)<<1)&Mask
        a,b=xor_sum,carry
        
    return a if a<=Max else ~(a^Mask)

print(get_sum(2,3))    
    