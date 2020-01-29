Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def about(name, age, likes):
	sentence = "Meet {}! They are {} years old and they like {}".format(name,age,likes)
	return sentence

>>> about("Jack", 23, "Python")
'Meet Jack! They are 23 years old and they like Python'
>>> #parameters here are name, age, likes and the arguments are Jack, 23, Python
>>> 
>>> #key word arguments
>>> about(age = 23, name = "Greg", likes = "football")
'Meet Greg! They are 23 years old and they like football'
>>> 
>>> #the arguments are required either postitional or keyword arguments
>>> 
>>> #assign default value parameters
>>> 
>>> about("Bill", 32, likes = "soccer")
'Meet Bill! They are 32 years old and they like soccer'
>>> about("James", 44, "baseball")
'Meet James! They are 44 years old and they like baseball'
>>> 
>>> about(name = "Cindy", likes = "flowers", age = 11)
'Meet Cindy! They are 11 years old and they like flowers'
>>> #default parameter must go at the end
>>> 
>>> 
