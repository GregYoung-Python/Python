Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> author = "bookauthorsareincreasingeachyear"
>>> author [-2]
'a'
>>> author [-5]
'h'
>>> word.index("each")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    word.index("each")
NameError: name 'word' is not defined
>>> author.index("each")
24
>>> author.index("year")
28
>>> author[author.index("each"):word.index("year")]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    author[author.index("each"):word.index("year")]
NameError: name 'word' is not defined
>>> author[author.index("each"):author.index("year")]
'each'
>>> author.index("author")
4
>>> author[author.index("author"):author.index("year")]
'authorsareincreasingeach'
>>> author[author.index("year"):]
'year'
>>> author[author.index("arein"):author.index("cre")]
'arein'
>>> "string are an iterable immutable data type meaning that you can step through the string data type, but it is not changeable".
