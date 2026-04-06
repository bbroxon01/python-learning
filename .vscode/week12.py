#lecture 3
#unit 1
#beginner
#predict the print order, then: what does test() print??
#what happens if you uncomment print(x)?
def first():
    print("A")
    second()
    print("B")

def second():
    print("C")
    
first()

def test():
    x=5 
    print(x)
    
test()
#print(x)
#does not work x is outside the def

#intermediate
def f1():
    f2()

def f2():
    f3()
    
def f3():
    print("Here")
    
f1()
#Stack: f3(), f2(), f1()

def calculate():
    result = 10 * 2
    #print(result)
calculate()
#print(result)
#error is result was never printed inside of local environment

#advanced

#unit 2
