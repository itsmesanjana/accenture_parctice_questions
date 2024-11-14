def second_smallest(arr):
    if len(arr)<2:
        return 0
    arr=sorted(set(arr))
    second_smallest_no=arr[1]
    return second_smallest_no

A=list(map(int,input().split()))
print("The second smallest no is ",second_smallest(A))