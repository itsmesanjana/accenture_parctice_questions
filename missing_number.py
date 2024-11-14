def missing_no(nums):
    n=len(nums)

    expected_sum=n*(n+1)//2
    
    actual_sum=sum(nums)
    
    return expected_sum-actual_sum

print(missing_no([3,0,1]))
        