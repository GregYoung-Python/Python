Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> students = {}
>>> students = {"Bob":25, "Dan":33, "Susan":40, "Sally":22, "Mary":20}
>>> students["Susan"]
40
>>> students["Sally"]
22
>>> students["Mary"]
20
>>> students["Bob"]
25
>>> #we are going to add "Fred" to the dictionary
>>> students["Fred"] = 25
>>> students["Fred"]
25
>>> students["Susan"] = 41
>>> students["Susan"]
41
>>> del students["Fred"]
>>> students["Fred"]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    students["Fred"]
KeyError: 'Fred'
>>> students.keys()
dict_keys(['Bob', 'Dan', 'Susan', 'Sally', 'Mary'])
>>> students["Fred"] = 25
>>> students.keys()
dict_keys(['Bob', 'Dan', 'Susan', 'Sally', 'Mary', 'Fred'])
>>> A = list(students.keys())
>>> A[0]
'Bob'
>>> A[5]
'Fred'
>>> students.values()
dict_values([25, 33, 41, 22, 20, 25])
>>> B = list(students.values())
>>> B[3]
22
>>> B[1:4]
[33, 41, 22]
>>> B[:3]
[25, 33, 41]
>>> B[1:]
[33, 41, 22, 20, 25]
>>> print(students)
{'Bob': 25, 'Dan': 33, 'Susan': 41, 'Sally': 22, 'Mary': 20, 'Fred': 25}
>>> students.items()
dict_items([('Bob', 25), ('Dan', 33), ('Susan', 41), ('Sally', 22), ('Mary', 20), ('Fred', 25)])
>>> C = list(students.items())
>>> C
[('Bob', 25), ('Dan', 33), ('Susan', 41), ('Sally', 22), ('Mary', 20), ('Fred', 25)]
>>> C[2:5]
[('Susan', 41), ('Sally', 22), ('Mary', 20)]
>>> del students["Mary"]
>>> students.items()
dict_items([('Bob', 25), ('Dan', 33), ('Susan', 41), ('Sally', 22), ('Fred', 25)])
>>> 
