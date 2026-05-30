'''
Set will not allow duplicate elements.
set{}
unordered
no indexing, no slicling
donot allow duplicates
'''
'''
#SET METHODS
add()
update()
pop()
remove()
'''
'''
#SET OPERATORS
union()
intersection()
difference()
issubset()
issuperset()
'''
#set methods
S={22,90,'madhu',89,22,90}#it not allow duplicate &unordered ,no index
print(type(S)) #check which type of operator
print(S)
S.add(125) #adding of numbers
print(S)
S.update({456,89,65,23,23,56}) #update --bulk data is adding
print(S)
S.pop() # it will delete the random element
print(S)
S.remove('madhu')#it remove particular element 
print(S)

#set Operations 
# UNION OPERATOR
s1={1,5,6}
s2={7,8,9}
print(s1.union(s2))

#INTERSECTION OPERATOR # it will print common element in both s1 and s2
s1={1,5,6}
s2={7,8,9,5}
print(s1.intersection(s2))

#difference() # it will print only set1 and delete the common element
s1={1,5,6,5,9}
s2={7,8,9}
print(s1.difference(s2))

#issuperset #   if s1 and s2 element are same than only print true
s1={1,5,6}
s2={1,5,6,8,9}
print(s1.issuperset(s2))

#isSubset #if s2 and s1 elements are same than only print true
s1={5,6,7,8,9,10}
s2={5,6,8,7,9}
print(s2.issubset(s1))