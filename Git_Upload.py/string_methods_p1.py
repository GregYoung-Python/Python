Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "text is the original words and form of a written or printed work".count("e")
4
>>> "text is the original words and form of a written or printed work. each person should know his own work. most people do that.".capitalize()
'Text is the original words and form of a written or printed work. each person should know his own work. most people do that.'
>>> 
>>> 
>>> line_item = "text is the original words and form of a written or printed work. each person should know his own work. most people do that."
>>> 
>>> line_item.count("e")
8
>>> line_item.count("the")
1
>>> y = "Each Letter In This Sentence Begins With A Capital Letter. We Can Change That."
>>> y.lower()
'each letter in this sentence begins with a capital letter. we can change that.'
>>> 
>>> y.upper()
'EACH LETTER IN THIS SENTENCE BEGINS WITH A CAPITAL LETTER. WE CAN CHANGE THAT.'
>>> print(y)
Each Letter In This Sentence Begins With A Capital Letter. We Can Change That.
>>> 
>>> y= y.upper()
>>> 
>>> print(y)
EACH LETTER IN THIS SENTENCE BEGINS WITH A CAPITAL LETTER. WE CAN CHANGE THAT.
>>> y = y.lower()
>>> print(y)
each letter in this sentence begins with a capital letter. we can change that.
>>> y = y.capitalize()
>>> 
>>> print(y)
Each letter in this sentence begins with a capital letter. we can change that.
>>> y
'Each letter in this sentence begins with a capital letter. we can change that.'
>>> y.title()
'Each Letter In This Sentence Begins With A Capital Letter. We Can Change That.'
>>> 
>>> y = y.title()
>>> y
'Each Letter In This Sentence Begins With A Capital Letter. We Can Change That.'
>>> y.islower()
False
>>> y.isupper()
False
>>> y.istitle()
True
>>> y.isalpha()
False
>>> "ThisTitleCaseStringHasNoSpacesInIt".isalpha()
True
>>> y.isdigit()
False
>>> "100038884329".isdigit()
True
>>> x = "thispieceoftextonlyhaslettersandnumbers"
>>> x.isalnum()
True
>>> x = "thispieceoftextonlyhaslettersandnumbers993482199375"
>>> x.isalnum()
True
>>> x = "thispieceoftextonlyhaslettersandnumbers993482199375 11"
>>> x.isalnum()
False
>>> 
