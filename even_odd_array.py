def label_even_odd(arr):
    result=" "
    for num in arr:
        if num%2==0:
            result += "even"
        else:
            result += "odd"
    return result

N=5
A=[1 , 2 , 3 , 5 , 5 ]
print(label_even_odd(A))
