'''
In computer science, selection sort is an in-place comparison sorting algorithm. 
It has an O(n²) time complexity, which makes it inefficient on large lists, 
and generally performs worse than the similar insertion sort
'''

a_list = [54,5,45,74,587,87,8,454,5,8,7,61,76,94,45,3,23,2,68,98,97,37,132,135,64,89,91,3,18]

def selection_sort(unsorted_list):
    print(unsorted_list)
    for i in range(len(unsorted_list)):
        sm_index = i
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[sm_index]:
                sm_index = j
        
        unsorted_list[sm_index], unsorted_list[i] = unsorted_list[i], unsorted_list[sm_index]
    
    print(unsorted_list)

selection_sort(a_list)