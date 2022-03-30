'''
In computer science, binary search, 
also known as half-interval search, 
logarithmic search, or binary chop, 
is a search algorithm that finds the position of a target value within a sorted array. 
Binary search compares the target value to the middle element of the array
'''
a_list = [54,5,45,74,587,87,8,454,5,8,7,61,76,94,45,3,23,2,68,98,97,37,132,135,64,89,91,3,18]

def binary_search(a_list, value, left_edge, right_edge):
    if left_edge <= right_edge:
        middle = left_edge + (right_edge - 1) // 2
        
        if a_list[middle] == value:
             return middle
        elif a_list[middle] < value:
            return binary_search(a_list, value, middle + 1, right_edge)
        else:
            return binary_search(a_list, value, left_edge, middle - 1)
    
    return -1

res = print(a_list, 8, 0, len(a_list)- 1)
if res != -1:
    print("Element is present at index", str(res))
else:
    print("Element is not present in array")

