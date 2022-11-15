mytuple =("apple","banana", "cherry","cherry")
# print(mytuple) 
# print(len(mytuple))
"""Tuple
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets."""




# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], 
# the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, 
# it means that the items have a defined order, 
# and that order will not change.

# Unchangeable
# Tuples are unchangeable, 
# meaning that we cannot change, add or remove 
# items after the tuple has been created.


# A tuple can contain different data types:
# Example
# A tuple with strings, integers and boolean values:

# tuple1 = ("abc", 34, True, 40, "male")

# type()
# From Python's perspective, tuples are defined as objects with the data type 'tuple':

# <class 'tuple'>
# Example
# What is the data type of a tuple?

# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))


# mytuple =("apple","banana", "cherry","cherry")

# newlist = list(mytuple)
# # print(type(newlist))
# newlist[0] ="dog"
# newlist.append('banku')
# # print(newlist)
# newTuple = tuple(newlist)

# print(newTuple)

# print(mytuple)


# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.


# friendsTuple =tuple(('kofi','kai','doe'))

# print(friendsTuple)


# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:

# Example
# Print the second item in the tuple:

# thistuple = (
#     "apple", "banana", "cherry", 
#     "orange", "kiwi", "melon", "mango"
# )
# print(thistuple[1:])


# Python - Update Tuples
# Tuples are unchangeable, meaning that you cannot 
# change, add, or remove items once the tuple is created.
# But there are some workarounds.

thistuple = ("apple", "banana", "cherry", "papaya", "pineapple",)
(q,*r,x)=thistuple
print(q)
print(r)
print(x)


