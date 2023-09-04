Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[(1,2),(1,3),(2,3),(1,1),(3,8)]
print(dict(l))
{1: 1, 2: 3, 3: 8}
a=dict(l)
a
{1: 1, 2: 3, 3: 8}
print(d.keys(a))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(d.keys(a))
NameError: name 'd' is not defined. Did you mean: 'id'?
print(a.keys())
dict_keys([1, 2, 3])
print(a.values())
dict_values([1, 3, 8])
l
[(1, 2), (1, 3), (2, 3), (1, 1), (3, 8)]
>>> a
{1: 1, 2: 3, 3: 8}
>>> a.keys()
dict_keys([1, 2, 3])
>>> for i in a.keys():
...     print(i)
... 
...     
1
2
3
>>> 1=2
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> str(1)=2
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
>>> for i in a.keys():
...     i=1
... 
...     
>>> print (i)
1
>>> for i in a.keys():
...     i=1
...     print(i)
... 
...     
1
1
1
>>> for i,j in l:
...     print(i,j)
... 
...     
1 2
1 3
2 3
1 1
3 8
