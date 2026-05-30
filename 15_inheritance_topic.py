'''
single - base clas 
multilevel inheritance - dervied form parent class
mutiple inheritance - dervied form father and mother
hierachical inheritance - sliblings
'''
#single
class parent():
    def output(self):
        print("iam the parent")
class child():
    def output(self):
        print("iam the child") 
s=parent()
c=child()
c.output()#child method
s.output()#parent method            

#Multilevel inheritance
class grandfather():
    def output(self):
        print("iam the grandfather")
class parent(grandfather):
    def output(self):
        print("iam the parent")
class child(parent):
    def output(self):
        print("iam the child")
v=grandfather()        
s=parent()
c=child()
c.output()#child method
s.output() 
v.output() 

#mutiple inheritance
class father():
    def output(self):
        print("iam father")        
class mother():
    def output(self):
        print("iam mother")  
class child():
    def output(self):
        print("iam child")
s=father()
y=mother()
v=child()          
s.output()
y.output()
v.output()


#hirerarical   
class father():
    def output(self):
        print("iam father")        
class mother():
    def output(self):
        print("iam mother")  
class child1():
    def output(self):
        print("iam child1")
class child2():
    def output(self):
        print("iam child2")        
s=father()
y=mother()
v=child1()
z=child2()
s.output()
y.output()
v.output()
z.output()                       