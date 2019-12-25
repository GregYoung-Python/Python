Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> book = "dictionaryofwebsterandbritanica"
>>> 
>>> book [3]
't'
>>> book [0:10:1]
'dictionary'
>>> book [12:19:1]
'webster'
>>> book [0:10:2]
'dcinr'
>>> book [12:19:2]
'wbtr'
>>> book [23:32:1]
'ritanica'
>>> book [22:32:1]
'britanica'
>>> book [23:32:2]
'rtnc'
>>> book [0:]
'dictionaryofwebsterandbritanica'
>>> book [12:]
'websterandbritanica'
>>> book [22:]
'britanica'
>>> book [0::2]
'dcinrowbtrnbiaia'
>>> book [22::2]
'biaia'
>>> book [0::2]
'dcinrowbtrnbiaia'
>>> book [:10]
'dictionary'
>>> book [:16:2]
'dcinrowb'
>>> book [:10]
'dictionary'
>>> book [::-1]
'acinatirbdnaretsbewfoyranoitcid'




