>>> our_list = ["Are", "We", "Try","Find", 1,2,3,4,5,6, "Seven", "Eight", "Nine"]
>>> D = our_list[0]
>>> D
'Are'
>>> E = our_list[4::2]
>>> E
[1, 3, 5, 'Seven', 'Nine']
>>> F = our_list[7:]
>>> F
[4, 5, 6, 'Seven', 'Eight', 'Nine']
>>> G = our_list[4:10] 
>>> G
[1, 2, 3, 4, 5, 6]
>>> H = our_list[10:]
>>> H
['Seven', 'Eight', 'Nine']
>>> Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> new_list = [1,3,5,7,9,11,13,15,17,[22,24,26,28,30],[40,42,44,46,48,50]]
>>> y = new_list[9][3:]
>>> y
[28, 30]
>>> x = new_list[:9]
>>> x
[1, 3, 5, 7, 9, 11, 13, 15, 17]
>>> z = new_list[:10]
>>> z
[1, 3, 5, 7, 9, 11, 13, 15, 17, [22, 24, 26, 28, 30]]
>>> A = new_list[9]
>>> A
[22, 24, 26, 28, 30]
>>> B = new_list[9][:3]
>>> B
[22, 24, 26]
>>> C = new_list[10][2:]
>>> C
[44, 46, 48, 50]
>>> 
