#list
a=()
print(type(a))

#type of operations 
'''
1. concatenation --(addind of two numbers)
2. Iteration -- (looping of elements)
3. membership operations
4. identify operators
5. repatations operators-- repeat the tuple values
'''
'''
list allow the duplicates.. (allow different type of elements)
allow indexig and slicing
immutable
'''
#indexing
s=(23,56,89,456,63,12,'sravs')
print(s[-1])

#slicing
s=(23,56,89,456,63,12,'sravs')
print(s[0:2:4])

#min, max,length,sum,
s=(23,56,89,456,63,12)
print(min(s))
print(max(s))
print(sum(s))
print(len(s))

#concatenation--adding of elements
s1=1,2,3
t1=4,8,6
print(s1+t1)

#repetation
c=(56,89,46,78)#repating the tuple value
print(c*3)

#iteration
c=(56,89,46,78)
for i in c:
 print(i)


#membership operator
#exmple:1
c=(56,89,46,78)
print(12 in c)
print(78 in c)

#example:2
s1=(56,89,46,78)
s2=(23,56,20,45)
s3=(56,89,46,78)
print(s1 is s2)
print(s1 is s3)