Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> our_tuple = 1,2,3,"A","B","C"
>>> type(our_tuple)
<class 'tuple'>
>>> our_tuple = (1,2,3,"A","B","C")
>>> our_tuple
(1, 2, 3, 'A', 'B', 'C')
>>> our_tuple[0:3]
(1, 2, 3)
>>> #list are muteable meaning they can be changed after they are created, tuples are
>>> #immutable meaning they can not be changed.
>>> our_list[5,10,15,20,25,30]

>>> our_list = [5,10,15,20,25,30]
>>> our_list [2] = 100
>>> our_list
[5, 10, 100, 20, 25, 30]
>>> our_tuple
(1, 2, 3, 'A', 'B', 'C')
>>> our_tuple[2] = "E"
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    our_tuple[2] = "E"
TypeError: 'tuple' object does not support item assignment
>>> A = [1,3,7,9,11]
>>> A
[1, 3, 7, 9, 11]
>>> tuple(A)
(1, 3, 7, 9, 11)
>>> A  = A + [14]
>>> A
[1, 3, 7, 9, 11, 14]
>>> A = tuple(A)
>>> A
(1, 3, 7, 9, 11, 14)
>>> (A,B,C) = 1,2,3
>>> A
1
>>> B
2
>>> C
3
>>> D,E,F = [1,2,3]
>>> D
1
>>> E
2
>>> F
3
>>> G,H,I = "789"
>>> G
'7'
>>> H
'8'
>>> I
'9'
>>> #if we have an iterable data type we can assign a tuple on the left and another tuple
>>> #on the right an assign different variable to them.
>>> 
