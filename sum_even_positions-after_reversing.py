def sum_even_positions_after_reversing(arr):
    n=len(arr)
    total_sum=0

    for i in range(n):
        reversed_index=n-1-i
        #reversed_index=9,8,7,6,5,4,3,2,1,0
        if reversed_index % 2 == 0:
            total_sum+=arr[i]
            #2+
    return total_sum

arr=[1,2,3,4,4,5,6,7,7,8,8]
result=sum_even_positions_after_reversing(arr)
print("Sum of even positions after reversing: ",result)