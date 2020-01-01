app_users = ["Alice", "Bob", "Cindy", "Bill", "Joey", "Susan", "Walter"]
print(len(app_users))

while True:
    print("Hello my name is William! ")
    name = input("What is your name?: ").strip().capitalize()

    if name in app_users:
        print("Hello {}! " .format(name))
        remove = input("Would you like to be removed from the list? (y/n)?: ").strip().lower()

        if remove == "y":
            print(app_users)
            app_users.remove(name)
            print(app_users)
        elif remove == "n":
                print("Great we are glad you have decided to stay with us!")
    
    else:
        print("Your name is not in the list yet {}".format(name))
        add_name = input("Would you like to be added to the list (y/n)?: ").strip().lower()
        if add_name == "y":
            print(app_users)
            app_users.append(name)
            print(app_users)
        elif add_name == "n":
            print("No problem let us know if you change your mind!")
            


>>> L =[1,3, 5, 7, 9, 11, 13]
>>> del L[0]
>>> print(L)
[3, 5, 7, 9, 11, 13]
>>> del L [4:]
>>> print(L)
[3, 5, 7, 9]
>>> 
>>> L = [1,3,5,7,9,11,13,15]
>>> del L[5:]
>>> L
[1, 3, 5, 7, 9]
>>> L = [1,3,5,7,9,11,13,15]
>>> del L[3]
>>> L
[1, 3, 5, 9, 11, 13, 15]



>>> A = [5,7,9,11,15,29,35,42,41]
>>> 
>>> A = A + [1,2,3]
>>> A
[5, 7, 9, 11, 15, 29, 35, 42, 41, 1, 2, 3]
>>> A = A + ["BCDEF"]
>>> A
[5, 7, 9, 11, 15, 29, 35, 42, 41, 1, 2, 3, 'BCDEF']
>>> A = A + list("GHIJKL")
>>> A
[5, 7, 9, 11, 15, 29, 35, 42, 41, 1, 2, 3, 'BCDEF', 'G', 'H', 'I', 'J', 'K', 'L']
>>> A = A + [14]
>>> A
[5, 7, 9, 11, 15, 29, 35, 42, 41, 1, 2, 3, 'BCDEF', 'G', 'H', 'I', 'J', 'K', 'L', 14]
>>> A = A + list(str(5,6,7,8,9,10))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    A = A + list(str(5,6,7,8,9,10))
TypeError: str() takes at most 3 arguments (6 given)
>>> A = A + list(str(567))
>>> A
[5, 7, 9, 11, 15, 29, 35, 42, 41, 1, 2, 3, 'BCDEF', 'G', 'H', 'I', 'J', 'K', 'L', 14, '5', '6', '7']
>>> 
>>> A = A + list(str(5678910))
>>> A
[5, 7, 9, 11, 15, 29, 35, 42, 41, 1, 2, 3, 'BCDEF', 'G', 'H', 'I', 'J', 'K', 'L', 14, '5', '6', '7', '5', '6', '7', '8', '9', '1', '0']
>>> A = [29,39,49,59]
>>> A = A + [[2,4,6,8]]
>>> A
[29, 39, 49, 59, [2, 4, 6, 8]]
>>> A[-1]
[2, 4, 6, 8]
>>> A[-2]
59
>>> A.append(100,101)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    A.append(100,101)
TypeError: append() takes exactly one argument (2 given)
>>> A.append(100)
>>> A
[29, 39, 49, 59, [2, 4, 6, 8], 100]
>>> A.append([100,101,103])
>>> A
[29, 39, 49, 59, [2, 4, 6, 8], 100, [100, 101, 103]]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> A
[29, 39, 49, 59, [2, 4, 6, 8], 100, [100, 101, 103]]
>>> A = A.append(10)
>>> A
>>> type(A)
<class 'NoneType'>
>>> A = []
>>> type(A.append(10))
<class 'NoneType'>
>>> A = [5,7,9,11,15,29,35,42,41]
>>> A
[5, 7, 9, 11, 15, 29, 35, 42, 41]
>>> A.insert(2,105)
>>> A
[5, 7, 105, 9, 11, 15, 29, 35, 42, 41]
>>> A.insert(7,222)
>>> A
[5, 7, 105, 9, 11, 15, 29, 222, 35, 42, 41]
>>> A.insert(3,[111,113,115,117])
>>> A
[5, 7, 105, [111, 113, 115, 117], 9, 11, 15, 29, 222, 35, 42, 41]
>>> #list are muteable meaning they can be changed.
>>> #strings are immuteable meaning they can't be changed.
>>> A[0] = 5
>>> A
[5, 7, 105, [111, 113, 115, 117], 9, 11, 15, 29, 222, 35, 42, 41]
>>> A[1] = 5
>>> A
[5, 5, 105, [111, 113, 115, 117], 9, 11, 15, 29, 222, 35, 42, 41]
>>> s = "12457"
>>> s[0]=2
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s[0]=2
TypeError: 'str' object does not support item assignment
>>> A.remove(5)
>>> A
[5, 105, [111, 113, 115, 117], 9, 11, 15, 29, 222, 35, 42, 41]
>>> A.remove([3])
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    A.remove([3])
ValueError: list.remove(x): x not in list
>>> A.remove(113)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    A.remove(113)
ValueError: list.remove(x): x not in list
>>> A.remove([[2]])
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    A.remove([[2]])
ValueError: list.remove(x): x not in list
>>> del A [2]
>>> A
[5, 105, 9, 11, 15, 29, 222, 35, 42, 41]
>>> 
