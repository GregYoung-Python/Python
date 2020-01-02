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

#dictionary inside of a dictionary

students = {
                  "Bob": {"id": "ID0001", "age": 22, "grade": "A"},
                  "Dan":{"id": "ID0002", "age": 27, "grade": "B"},
                  "Susan":{"id": "ID0003", "age": 31, "grade": "C"},
                  "Sally":{"id": "ID0004", "age": 33, "grade": "D"},
                  "Mary":{"id":"ID0005", "age": 25, "grade": "E"},
                  "Alice":{"id":"ID0006", "age":36, "grade": "A"}
            }

print(students["Bob"]["id"], students["Bob"]["age"], students["Bob"]["grade"])
print(students["Dan"]["id"], students["Dan"]["age"], students["Dan"]["grade"])
print(students["Susan"]["id"], students["Susan"]["age"], students["Susan"]["grade"])
print(students["Sally"]["id"], students["Sally"]["age"], students["Sally"]["grade"])
print(students["Mary"]["id"], students["Mary"]["age"], students["Mary"]["grade"])
print(students["Alice"]["id"], students["Alice"]["age"], students["Alice"]["grade"])  
