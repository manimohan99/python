"""
Lists — indexing, slicing, mutability, list methods 
Tuples and immutability use cases 
Sets, set operations 
Dictionaries — keys, values, get(), update(), iteration 
List and dict comprehensions 
""" 
# list  it is order and mutable collections 

"""a=[1,2,3,4,5]
b=a
b.append(6)
print(a)"""

"""b=[1,2,4,5,6]
print(b*3)"""

"""a=[1,2,3,4,5,6]
print(a[::2])"""
 
"""be=[1,2,3,4,5,6]
print(sum(be,10))"""

#What is the difference between append() and extend() in lists?
"""list = [1,2,3,4,5,6]
print1=(list.append([7,8]))
print2=(list.extend([123,12]))
print(list[3])"""

"""#list comprehension examples 
list1= [1,3,4,5,5,6]
square=[x*2 for x in list1 ]
print(square)"""

#touples are immutable collections 
""""tuple1=(2,3,4,5,6)
print(tuple1[2])"""

#slicing in tuple
"""tuple1=(2,3,4,5,6)
print(tuple1[1:4])"""

#more methods in this 
"""tuple1=(2,3,4,5,6)
print(tuple1.count(3))"""

 #more tricky example of tuple
""""tuple1=(2,3,4,5,6)
print(tuple1.index(4))"""

#
# how to convert tuple to list and list to tuple
"""tuple1=(2,3,4,5,6)
list1=list(tuple1)
print(list1)
tuple2=tuple(list1)
print(tuple2)"""

#tricky examples of sets
"""set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
print(set1.union(set2))"""

#some
# more examples of sets and set operations with list
#


"""set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))"""
#Dictionaries — keys, values, get(), update(), iteration 
#List and dict comprehensions 

"""dict1={'a':1,'b':2,'c':3}
print(dict1['a'])"""

"""dict1={'a':1,'b':2,'c':3}
print(dict1.get('d',4))"""

"""dict1={'a':1,'b':2,'c':3}
dict1.update({'d':4})
print(dict1)"""

#some more examples of list and dict comprehensions with dsa level questions
"""dict1={'a':1,'b':2,'c':3}
squared_dict1={k:v**2 for k,v in dict1.items()}
print(squared_dict1)"""

"""dictinary1={'name':'john','age':30,'city':'new york'}
print(list(dictinary1.keys())[1])
print(list(dictinary1.values())[1])]
"""

