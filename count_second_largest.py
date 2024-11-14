def count_second_largest(arr):
    if len(arr)<2:
        return 0
    arr=sorted(set(arr))
    second_largest=arr[1]
    print(f"The second largest no is {second_largest}")
    count=arr.count(second_largest)
    return count

A=list(map(int,input().split()))
print(f"It has occured {count_second_largest(A)} times")
    