def check_reverse(arr):
    n=len(arr)
    temp=arr[:]
    temp.sort()
    start=0
    while start<n and temp[start]==arr[start]:
        start+=1
    end=n-1
    while end>=0 and temp[end]==arr[end]:
        end-=1 
    
    if start>=end:
        return True
    
    while start>end:
        if arr[start]<arr[start-1]:
            return False
        start-=1
    return True

arr=[1,2,5,4,3]
print("YES" if check_reverse(arr) else "NO")