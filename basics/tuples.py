# Tuples : Ordered, Immutable, allows Duplicate elements
my_tuple = ("23", 76, "Hello") # use parantheses
my_tuple1 =  "23", 76, "Hello" # still creates a tuple
my_tuple2 = ("23") # a string
my_tuple3 = ("23",) # a tuple
my_tuple4 = "23", # tuple
print(type(my_tuple))
print(type(my_tuple1))
print(type(my_tuple2))
print(type(my_tuple3))
print(type(my_tuple4))

print("\n")
# tuple from a list 
my_tuple1 = tuple([1,2,3,4,5,6])
print(my_tuple1)

print("\n")
# access a tuple with indexes 
item = my_tuple1[0]
print(item) # first item
print(my_tuple1[-1]) # last item
print(my_tuple1[5]) # last item

# can not add as tuples are immutable
# item[1] = 4
# print(item)

print("\n")

# iterate 
for i in my_tuple1:
    print(i)

a = ("Hello", 42, "World")
if "Hello" in a:
    print("yes")
else:
    print("no")

print("\n")

# get the number of elements in a tuple
print(len(a))

# count ocurance 
b = ('h', 'e', 'l', 'low','o','r','l','d')
print(b.count('l'))

# return the index of 
print(b.index('o'))

# convert a tuple to a list and back
my_list = list(b)
my_tuple_b = tuple(my_list)
print(my_list)
print(my_tuple_b)