# # Lists: Ordered, Mutable, allows Duplicate elements
# # you can create a list with [] brackets
# my_list = []
# print(my_list)

# # or use the list function from python std library
# my_list1 = list()
# print(my_list1)

# #  or create and initialise 
# my_list2 = ["banana", "cherry", "apple"]
# print(my_list2)

# # a list allows different data types & duplicates
# my_list3 = [6, True, 7.4, "cruixer", "cruixer"]
# print(my_list3)

# # access a list with indexes 
# item = my_list3[0]
# print(item) # first item
# print(my_list3[-1]) # last item
# print(my_list3[4]) # last item

# # iterate through a list
# # for loop:
# for i in my_list3:
#     print(i)

# # check if element is in list
# if "banana" in my_list2:
#     print("yes")
# else:
#     print("no")

# # check/count the number of elements in a list
# print(len(my_list3))

# # add elements to a list,.. adds to the end
# my_list.append("H")
# my_list.append("E")
# my_list.append("L")
# my_list.append("L")
# my_list.append("0")
# print(my_list)

# # add elements to a list,.. adds at specified index
# my_list2.insert(2, "WORLD")
# print(my_list2)

# # remove elements/items
# item = my_list3.pop() # return the lat items and removes it
# print(item)
# print(my_list3)

# # remove a specific element
# my_list2.remove("WORLD")
# print(my_list2)

# # remove all elements
# my_list2.clear()
# print(my_list2)

# # reverse the order of elements in a list
# my_list3.reverse()
# print(my_list3)

# # sort a list, ascending order
# num_list = [2, 3, 9, -48, 4, -12, 5, 8, 9, 4, -8, 7]
# item = num_list.sort() # note that the sort function changes the original list
# print(item)
# print(num_list)
# # to fix the above
# num_list = [2, 3, 9, -48, 4, -12, 5, 8, 9]
# newnum_list = sorted(num_list)
# print(newnum_list)
# print(num_list) # note the list did not change

# # list short hands
# my_list4 = [1] * 6
# print(my_list4)

# # adding two lists
# list_add = num_list + my_list4
# print(list_add)

# # slicing list[start:stop] //excludes index at stop
# a = list_add[3: 8]
# print(a)
# b = list_add[:9] # starts from index 0
# c = list_add[7:] # to the last index
# print(b)
# print(c)

# # stepping/skipping
# d = b[::1] # default does not skip
# e = b[::2] # takes every second element
# print(d)
# print(e)
# f = b[::-1] # reverses the list :p
# print(f)

# # copying lists
# a = b
# a.append(4) # this modifies b too
# print(a)
# print(b)
# a.pop()
# # to fix the above
# print("\n")
# a = b.copy()
# a.append(4) # this modifies b too
# print(a)
# print(b)
# # or
# a = list(b)
# a.append(4) # this modifies b too
# print(a)
# print(b)
# # or
# a = b[:] # slice all
# a.append(4) # this modifies b too
# print(a)
# print(b)

# # list comprehension 
# b = [i**2 for i in a] # square every element of a and save in b
# print(a)
# print(b)

