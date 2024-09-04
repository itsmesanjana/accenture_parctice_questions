def find_positive_mid_element(arr):
    # Filter out negative numbers
    positive_arr = [num for num in arr if num >= 0]

    # Calculate the mid-index
    length = len(positive_arr)
    mid_index = length // 2

    # If the length is even, take the smaller of the two mid elements
    if length % 2 == 0:
        return min(positive_arr[mid_index - 1], positive_arr[mid_index])
    else:
        return positive_arr[mid_index]

# Input reading and processing
n = int(input())
arr = list(map(int, input().split()))

# Output the result
print(find_positive_mid_element(arr))

