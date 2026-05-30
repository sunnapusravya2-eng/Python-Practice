'''
int (1,-1)
float(1.2)
boolean (true or false)
complex
'''
#int type conversion 
a=1
b=-22
print(type(a),type(b))

#float type conversion 
a=1.4
print(type(a))

#boolean type conversion 
a=True
b=False
print(type(a),type(b))

#complex type conversion 
v=2+6j
print(type(v))

#implicit type conversion <---no data loss 
#smaller date type to larger data type 
a=2
print(float(a))

#explict type conversion<--data loss 
#also called type casting 
c=77.4
print(int(c))