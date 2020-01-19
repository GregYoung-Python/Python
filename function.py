Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x,y):
	return x+y

>>> add(20,10)
30
>>> def can(z,b):
	return z+b

>>> can(40,40)
80
>>> 
>>> answer = can(100,20)
>>> answer
120
>>> answer = add(30,40)
>>> answer
70
>>> #printing functions is not the same as returning the answer
>>> #printing only  shows the answer on the screen.
>>> 
>>> def add(x,y):
	print x+y
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x+y)?
>>> def add(x,y):
	print (x+y)

	
>>> add(7,7)
14
>>> answer = add(7,8)
15
>>> answer
>>> #cannot store a variable using the print function
>>> type(answer)
<class 'NoneType'>
>>> 
>>> word = "orange"
>>> word[::-1]
'egnaro'
>>> 
>>> 
>>> def rev(text):
	return text[::-1]

>>> rev("school")
'loohcs'
>>> rev([1,2,3,4,5,6,7,8])
[8, 7, 6, 5, 4, 3, 2, 1]
>>> 
>>> def multiply(x,y):
	return x*y

>>> multiply(10,2)
20
>>> def divide(c,d):
	return c/d

>>> divide(1000,200)
5.0
>>> 
>>> def subtract(v,m):
	return v - m

>>> subtract (80,60)
20
>>> 

>>> rev("ground")
'dnuorg'
>>> 



