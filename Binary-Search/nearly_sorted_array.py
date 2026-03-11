from typing import List    
def nearly_sorted_binary_search(arr: List, t: int)->int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            if mid + 1 < len(arr) and arr[mid + 1] == t:
                return mid + 1
            left = mid + 1
        else:
            if mid - 1 >= 0 and arr[mid - 1] == t:
                return mid - 1
            right = mid - 1
    return -1

arr=[2,1,4,3,6,5]
t=1
print(nearly_sorted_binary_search(arr, t))