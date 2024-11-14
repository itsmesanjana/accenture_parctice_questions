# def rotate_array(arr,k):
#     n=len(arr)
#     k=k%n

#     rotate_array=arr[-k:]+arr[: -k]
#     # arr[-k:]: This retrieves the last k elements of the array. In this example, for k = 3, arr[-3:] gives [5, 6, 7]
# # arr[:-k]: This retrieves the first n - k elements (i.e., the elements before the last k elements). In this example, for k = 3, arr[:-3] gives [1, 2, 3, 4].
#     return rotate_array

# arr=[1,2,3,4,5,6,7]
# k=5
# result=rotate_array(arr,k)
# print("Rotated Array:",result)

def rotate_array(arr,k):
    n=len(arr)
    k=k%n

    rotate_array=arr[-k:]+arr[:-k]
    return rotate_array

arr=[1,2,3,4,5,6,7]
k=5
result=rotate_array(arr,k)
print("Rotated Array:",result)

    