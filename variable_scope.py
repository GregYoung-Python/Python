a = 100
b = 2000
# this is a global variable 
def f1():
    print(a)

def f2():
    print(a)


f1()
f2()

# b is not a global variable here
def f3():
    # b = 200
    b = a + 10
    print(b)

def f4():
    b = 50
    print(b)

f3()
f4()
print(b)
print(a)

#change the global value inside the function

def f5():
    global a
    a = 300
    print(a)
f5()
print(a)

