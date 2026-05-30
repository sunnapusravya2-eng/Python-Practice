'''
{}
key:value Data
value should be muttable
key will act as Index
no scling
keys are unique
{'a':2,'b':123}# key +value = item 
'''
'''
dict methoods
get()
update()
values()
keys()
items()
'''
a={}
print(type(a))

#dict program
d={2:"sravya","YASH":45,"JASHU":19}
print(d["YASH"])

#get() -- get is only access key value
d={22:'sravya',26:'yash',20:'jashu'}
print(d.get(20))

#key()-- it will access all keys
d={22:'sravya',26:'yash',20:'jashu'}
print(d.keys())

#value()it will access all key values
d={22:'sravya',26:'yash',20:'jashu'}
print(d.values())

#items() it will acess all keys and values 
d={22:'sravya',26:'yash',20:'jashu'}
print(d.items())

#update()
d={22:'sravya',26:'yash',20:'jashu'}
d.update({45:'madhu'})
print(d)

#using for loop in dict
for i in {22:'sravya',26:'yash',20:'jashu'}.values():
    print(i)
    





