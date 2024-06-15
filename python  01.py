Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(10)
10
a=10
print(type(a))
<class 'int'>
a=suriya
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a=suriya
NameError: name 'suriya' is not defined
print(suriya)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(suriya)
NameError: name 'suriya' is not defined
>>> a='suriya'
>>> print(type(a))
<class 'str'>
>>> import datetime as dt
>>> dt.datetime.now().date()
datetime.date(2024, 6, 15)
>>> import calendar as cl
>>> print(cl.Calendar(2024))
<calendar.Calendar object at 0x00000253639E97F0>
>>> print(cl.FEBRUARY(2024))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(cl.FEBRUARY(2024))
TypeError: 'Month' object is not callable
>>> print(cl.'FEBRUARY'(2024))
SyntaxError: invalid syntax
>>> print(cl.'FEBRUARY'(2024))
SyntaxError: invalid syntax
>>> print(cl.FEBRUARY(2024))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(cl.FEBRUARY(2024))
TypeError: 'Month' object is not callable
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> keyword.issoftkeyword
<built-in method __contains__ of frozenset object at 0x000002536139B060>
>>> KeyboardInterrupt
>>> keyword.softkwlist
['_', 'case', 'match', 'type']
>>> keyword.iskeyword
<built-in method __contains__ of frozenset object at 0x000002536139AF80>
>>> 
>>> print('_')
_
>>> print(type('_'))
<class 'str'>
