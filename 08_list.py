'''
mutable,we can change data or modify the data
Heterogeneous objects are allowed. means List will allow different data type elements  
append
extend
count
insert
pop
remove
index
'''
#type check
v=[]
print(type(v))

#indexing
v=[2,'sravs',55,67,89]
print(v[3]) #postive index
print(v[-1]) #negtive index

#slicing
#  0  1  2  3   4       5  
v=[59,69,78,56,'sravs','yash']
print(v[2:56:2]) #start:stop:skip

#append --- addind data
y=[1,2.3,78,99,50,'yash']
y.append('sravs')
print(y)

#extend --- adding bulk amount of data
y=[23,53,66,88]
y.extend([58,55,90,'sai'])
print(y)

#count #counting the elements
y=['sravs','yash',23,53,26,23]
print(y.count(23))

#pop--- remove 
y=['sravs','yash',23,53,26,23]
y.pop(-2)
print(y)#remove based on indexing

#remove -- REMOVE PARTICULAR ELEMENT 
y=[23,56,89,43,58]
y.remove(56)
print(y)

#insert
y=[90,78,'sravs',28]
y.insert(3,'yash')
print(y)