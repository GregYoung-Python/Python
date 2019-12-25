Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> x = "i'm looking for a mouse in a big brown house"
>>> x.index("big")
29
>>> x.find("big")
29
>>> x.find("aiaiaijjjj")
-1
>>> x.index("ajaiaijjj")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x.index("ajaiaijjj")
ValueError: substring not found
>>> x = "111111i'm looking for a mouse in a big brown house11111"
>>> x.strip("1")
"i'm looking for a mouse in a big brown house"
>>> x = "jjjjjjji'm looking for a mouse in a big brown housejjjjjj"
>>> x.strip("j")
"i'm looking for a mouse in a big brown house"
>>> x
"jjjjjjji'm looking for a mouse in a big brown housejjjjjj"
>>> x.lstrip("j")
"i'm looking for a mouse in a big brown housejjjjjj"
>>> x.rstrip("j")
"jjjjjjji'm looking for a mouse in a big brown house"
>>> x.strip("j")
"i'm looking for a mouse in a big brown house"
>>> name = input("What is your name?: ")
What is your name?:    Greg   
>>> print(name)
   Greg   
>>> len(name)
10
>>> name = input("What is your name?: ").strip()
What is your name?:     Greg    
>>> print(name)
Greg
>>> len(name)
4
>>> 
