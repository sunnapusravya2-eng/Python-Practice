'''
function-- block of code, run when its is called
#syntax
def function nam():}-- function defination
function body
function.name}--function call

'''
#syntax
def func():#function call
    print("this is function call") #function body
func() #function call

#arbatiry Arguments # by using ["*"] we can use one argummnets with multiple function call
def func(*a):#function call
    print("this is function call",a) #function body
func(1,2,3) #function call

#key word arguments
def func(**a):
    print("this is function",a)
func(a=1,b=2)

#nested function -- function with in a function 
def outer ():
    print("outer function")
def inner (): 
    print("inner function")
inner()    
outer()

# example
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
add(3,3)
sub(6,3)
        
    
 