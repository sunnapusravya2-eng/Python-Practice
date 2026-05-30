#looping statements
'''
for
while
nested loop
'''
#example1 print 1 to 20 numbers 
for i in range (0,20):
    print(i)
    
#example2
a='sravya'
for i in a:
    print(a) 
    
#example3
a=[1,5,5.0,5]
for i in a:
    print(a)    
 
 #while statement 
 #example 1
 #Here i  value 1
 
i=1
while i<=5:
    print(i)
    i+=1
    
#example 2 print even numbers 
i=2
while i<=10:
 print(i)
 i+=2   
#
for i in range (1):
 print(i)
i+=9

#squares
for i in range (5):
    print(i*i)
    
#example 3 print reverse of numbers
i=6
while i>=1:
    print(i)
    i-=1
      
    
#nested loop--loop inside another loop 
'''
syntax
for i in range(....)
for j in rage(....)
print(i,j)
''' 

#example 1
for i in range(4,5,6):   
 for j in range(7,8,9):
  print(i,j)