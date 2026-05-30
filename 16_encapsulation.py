'''
wraping of variables and methods into single unit 
varible+methods=encapsulations
access specifier
private
public
protected
'''

 #encapsulation_abstraction.py >
class demo():
    def __init__(self,a,b):
        self._a=a # private
        self._b=b# protected
class demo2(demo):
    def output(self):
        print(self._a)
d=demo2(3,4)
d.output() 