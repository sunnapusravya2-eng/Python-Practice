'''
shallow copy 
deep copy
'''
#shallow copy
print("shallow copy:")
l1=[1,2,3]
l2=l1.copy() #l2=1,2,3
l1[0]=10
print(l1)
print(l2)

#deep copy -- 2d array
print("deep copy:")
import copy
a=[
    [7,8,9],
    [5,6,2]
   ]
b=copy.deepcopy(a)#here b=7.8,9,,5,6,2
a[0][0]=10
print(a)
print(b)

#deep copy
print("deep copy1:")
import copy
l1=[[1,2,3],[4,5,6]]
l2=copy.deepcopy(l1)
l1[0][0]=10
print(l1)
print(l2)
print()

