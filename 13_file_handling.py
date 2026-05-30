'''
file handling {reading,writing,delete,create}
#modes
r - read
w - write(truncate)
a - append
r+ - read/write
W+ - write/read(truncate)
'''

s=open('demo.text',mode='r')
print(s.read())
s.close() 
    