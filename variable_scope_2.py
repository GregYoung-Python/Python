a = [1,2,3,4,5]

def f1():
    a = 10
    print(a)
f1()
print(a)


#change global value inside of a list
def f2():
    a[0] = 5
    print(a)

f2()

print(a)

