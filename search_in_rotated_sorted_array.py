def search_in_rotated_storted_array(nums,target):
    n=len(nums)
    
    for i in range(n):
        if nums[i]==target:
         return i
    return -1

nums=list(map(int,input().split()))
target=int(input("Enter target value here: "))
print(search_in_rotated_storted_array(nums,target))