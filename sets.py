# myset = {1, 2, 3}

# mydict = {
#     1: 3,
#     4: 5,
#     9: 10,
# }

# newset = {}
# print(type(newset))

# union 

# both are for union 
# s = s1 | s2 
# print(s1.union(s2))

# both are for intersection 
# s = s1 & s2 
# print(s)
# print(s1.intersection(s2))

# both are differences 
# s = s1 - s2 
# print(s)
# print(s1.difference(s2))

# s = (s1 | s2) - (s1 & s2)
# print(s)
# print(s1.symmetric_difference(s2))
# s = s1.union(s2) - s1.intersection(s2)
# print(s)

# cardinality 

# print(len(s1))

# s = {}

# news = set(s)

# s = set()
# print(type(s))

# Disjoint sets 

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}

# intersect = s1 & s2 
# if len(intersect) > 0: 
#     print("It is not disjoint")
# else:
#     print("It is disjoint")

# Q. find all the unique elements from this list 
# mylist = [1, 2, 2, 2, 3, 4]
# s = set(mylist)
# print(s)

# set() will convert every iterable into set 
# mystring = "aaaaabshaaaaaabbbbsssiohi"
# s = set(mystring)
# print(s)



# s1 should be either the part of s2 or exactly same as s2 (s1 is subset of s2)
# print(s1 <= s2)

# s = s1.issubset(s2)
# print(s)

# s1 is proper subset of s2 i.2 it is a part of s2 
# print(s1 < s2)

# s1 = {1, 2, 3, 4}
# s2 = {1, 2, 3, 4}

# print(s2 >= s1)
# s = s2.issuperset(s1)
# print(s)

# mytuple = (1, 2, 3, 4)

# print(type(mytuple))
# print(id(mytuple))
# it will give an error 
# mytuple[1] = 10
# mytuple = (9, 0, 8, 7)

# print(type(mytuple))

# print(id(mytuple))

# i think something is wrong with your headphones maybe 
# no voice 

# print(mytuple)

# frozen sets = immutable sets 
# s1 = {1, 2, 3, 4}
# s1[0] = 10 
# print(s1)

# s = frozenset(s1)
# s[2] = 30 
# print(s)

# x = 12
# y = 3
# z = 11
# if (x == 2 and x < 3):
#     print(x)
# if x != 5:
#     print("whatever")
# if x != 5 and y >= 5 and z <= 13:
#     print("its gonna happen")
# if z != 0 or x == 2:
#     print("you say")
# if (not(y < 10)):
#     print(y)
# elif(x < 10 or x < 5):
#     print("okkkkkkk")
# elif(y < 10 or y <= 0):
#     print("pikachu")
# elif(z == 0 or y ==5):
#     print("Pikaboo")
# else:
#     print("Default value")


# functions 
# 3, 3, 15, 14, 3, 33 

# x = 3 
# print(x)
# def func(x):
#     print(x)
#     x += 12 
#     print(x)
#     x -= 1 
#     print(x)
#     return x 

# print(x)
# x = func(22)
# print(x)

# 0, 1, 2, 3 
# for i in range(6):
#     if i == 0: 
#         print(i)
#     if i >= 0: 
#         print(i+1)
#     if i == 2: 
#         continue 
#     if i < 4: 
#         break 
#     elif i == 4: 
#         print(i)
#     else: 
#         print("default")
    