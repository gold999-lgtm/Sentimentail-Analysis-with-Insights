Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import heapq
>>> from collections import Counter
>>> from operator import itemgetter
>>> x=[3,5,1,2,9,11,6]
>>> heapify(x)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    heapify(x)
NameError: name 'heapify' is not defined
>>> import heapq
>>> from collections import Counter
>>> from operator import itemgetter
>>> x=[3,5,1,2,9,11,6]
>>> heapq.heapify(x)
>>> print(x)
[1, 2, 3, 5, 9, 11, 6]
>>> t={}
>>> for i in range(0,len(x)):
	c=0
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			c=c+1
			t[x[i]]=c
	print(t)

	
{}
{}
{}
{}
{}
{}
{}
>>> import heapq
>>> from collections import Counter
>>> from operator import itemgetter
>>> x=[3,5,1,2,9,11,6,3,6,1,8,2,9,3,5]
>>> heapq.heapify(x)
>>> print(x)
[1, 1, 2, 2, 5, 3, 3, 3, 6, 9, 8, 11, 9, 6, 5]
>>> t={}
>>> for i in range(0,len(x)):
	c=0
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			c=c+1
			t[x[i]]=c
	print(t)

	
{1: 1}
{1: 1}
{1: 1, 2: 1}
{1: 1, 2: 1}
{1: 1, 2: 1, 5: 1}
{1: 1, 2: 1, 5: 1, 3: 2}
{1: 1, 2: 1, 5: 1, 3: 1}
{1: 1, 2: 1, 5: 1, 3: 1}
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1}
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1, 9: 1}
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1, 9: 1}
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1, 9: 1}
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1, 9: 1}
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1, 9: 1}
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1, 9: 1}
>>> for i in range(0,len(x)):
	c=0
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			c=c+1
			t[x[i]]=c

>>> print(t)
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1, 9: 1}
>>> for i,j in nlargest(3,t.items(),key=itemgetter(1)):
	print(i,j)

	
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    for i,j in nlargest(3,t.items(),key=itemgetter(1)):
NameError: name 'nlargest' is not defined
>>> for i,j in heapq.nlargest(3,t.items(),key=itemgetter(1)):
	print(i,j)

	
1 1
2 1
5 1
>>> for i in range(0,len(x)):
	c=1
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			c=c+1
	t[x[i]]=c

	
>>> print(t)
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1, 9: 1, 8: 1, 11: 1}
>>> for i in range(0,len(x)):
	c=x.Counter(i)
	t[x[i]]=c

	
Traceback (most recent call last):
  File "<pyshell#43>", line 2, in <module>
    c=x.Counter(i)
AttributeError: 'list' object has no attribute 'Counter'
>>> for i in range(0,len(x)):
	c=x.Count(i)
	t[x[i]]=c

	
Traceback (most recent call last):
  File "<pyshell#45>", line 2, in <module>
    c=x.Count(i)
AttributeError: 'list' object has no attribute 'Count'
>>> x=[3,5,1,2,9,11,6]
>>> x=[3,5,1,2,9,11,6,3,6,1,8,2,9,3,5]
>>> for i in range(0,len(x)):
	c=x.Count(x[i])
	t[x[i]]=c

	
Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    c=x.Count(x[i])
AttributeError: 'list' object has no attribute 'Count'
>>> for i in range(0,len(x)):
	c=1
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			c=c+1
	t[x[i]]=c

	
>>> print(t)
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1, 9: 1, 8: 1, 11: 1}
>>> for i in range(0,len(x)):
	
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			c=c+1
	t[x[i]]=c

	
>>> c=0
>>> for i in range(0,len(x)):
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			c=c+1
	t[x[i]]=c

	
>>> print(t)
{1: 8, 2: 8, 5: 8, 3: 8, 6: 8, 9: 8, 8: 8, 11: 6}
>>> print(x)
[3, 5, 1, 2, 9, 11, 6, 3, 6, 1, 8, 2, 9, 3, 5]
>>> for i in range(0,len(x)):
	c=1
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			c=c+1
	t[x[i]]=c

	
>>> print(t)
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1, 9: 1, 8: 1, 11: 1}
>>> for i in range(0,len(x)):
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			c=c+1
	t[x[i]]=c
	c=1

	
>>> print(t)
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1, 9: 1, 8: 1, 11: 1}
>>> for i in range(0,len(x)):
	c=1
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			c=c+1
		else:
			continue
	t[x[i]]=c

	
>>> print(t)
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1, 9: 1, 8: 1, 11: 1}
>>> for i in range(0,len(x)):
	c=1
	j=i+1
	while j<len(x):
		if x[i]==x[j]:
			c=c+1
			j=j+1
		else:
			j=j+1

			
>>> for i in range(0,len(x)):
	c=1
	j=i+1
	while j<len(x):
		if x[i]==x[j]:
			c=c+1
			j=j+1
		else:
			j=j+1
	t[x[i]]=c

	
>>> print(t)
{1: 1, 2: 1, 5: 1, 3: 1, 6: 1, 9: 1, 8: 1, 11: 1}
>>> print(x)
[3, 5, 1, 2, 9, 11, 6, 3, 6, 1, 8, 2, 9, 3, 5]
>>> t={}
>>> 
>>> for i in range(0,len(x)):
	c=1
	j=i+1
	while j<len(x):
		if x[i]==x[j]:
			c=c+1
			j=j+1
		else:
			j=j+1
	t[x[i]]=c

	
>>> print(t)
{3: 1, 5: 1, 1: 1, 2: 1, 9: 1, 11: 1, 6: 1, 8: 1}
>>> x=[2,5,1,6,9,1,2,6,3,4,5,3,1,2,2,2,2,8,7,7,9]
>>> t={}
>>> for i in range(0,len(x))
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntaxfor i in range(0,len(x))
SyntaxError: invalid syntax
>>> x=[2,5,1,6,9,1,2,6,3,4,5,3,1,2,2,2,2,8,7,7,9]
>>> t={}
>>> 

>>> for i in range(0,len(x)):
	c=1
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			c=c+1
	t[x[i]]=c

	
>>> print(t)
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
>>> for i in range(0,len(x)):
	c=1
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			c=c+1
t[x[i]]=c
SyntaxError: invalid syntax
>>> t[x[i]]=c
>>> print(t)
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
>>> 
>>> for i in range(0,len(x)):
	c=1
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			c=c+1
	print(x[i],c)

	
2 6
5 2
1 3
6 2
9 2
1 2
2 5
6 1
3 2
4 1
5 1
3 1
1 1
2 4
2 3
2 2
2 1
8 1
7 2
7 1
9 1
>>> for i in range(0,len(x)):
	c=1
	for j in range(i+1,len(x)):
		if x[i]==x[j]:
			if x[i] not in t:
				c=c+1
	if x[i] not in t:
		t[x[i]]=c
	print(t)

	
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
{2: 1, 5: 1, 1: 1, 6: 1, 9: 1, 3: 1, 4: 1, 8: 1, 7: 1}
>>> 
>>> t={}
>>> for i in range(0,len(x):
	       
SyntaxError: invalid syntax
>>> t={}
>>> for i in range(0,len(x)):
	t=t+x[i]

	
Traceback (most recent call last):
  File "<pyshell#126>", line 2, in <module>
    t=t+x[i]
TypeError: unsupported operand type(s) for +: 'dict' and 'int'
>>> for i in range(0,len(x)):
	x.count(x[i])

	
6
2
3
2
2
3
6
2
2
1
2
2
3
6
6
6
6
1
2
2
2
>>> for i in range(0,len(x)):
	c=x.count(x[i])

	
>>> t={}
>>> for i in range(0,len(x)):
	c=x.count(x[i])
	t[x[i]]=c

	
>>> print(t)
{2: 6, 5: 2, 1: 3, 6: 2, 9: 2, 3: 2, 4: 1, 8: 1, 7: 2}
>>> import heapq
>>> from collections import Counter
>>> from operator import itemgetter
>>> x=[3,5,1,2,9,11,6]
>>> heapq.heapify(x)
>>> print(x)
[1, 2, 3, 5, 9, 11, 6]
>>> x=[2,5,1,6,9,1,2,6,3,4,5,3,1,2,2,2,2,8,7,7,9]
>>> heapq.heapify(x)
>>> print(x)
[1, 2, 1, 2, 4, 1, 2, 5, 3, 7, 5, 3, 2, 2, 2, 6, 6, 8, 7, 9, 9]
>>> t={}
>>> for i in range(0,len(x)):
	c=x.count(x[i])
	t[x[i]]=c

	
>>> print(t)
{1: 3, 2: 6, 4: 1, 5: 2, 3: 2, 7: 2, 6: 2, 8: 1, 9: 2}
>>> for i,j in heapq.nlargest(3,t.items(),key=itemgetter(1)):
	print(i,j)

	
2 6
1 3
5 2
>>> import heapq
>>> from operator import itemgetter
>>> x=[2,5,1,6,9,1,2,6,3,4,5,3,1,2,2,2,2,8,7,7,9]
>>> heapq.heapify(x)
>>> t={}
>>> for i in range(0,len(x)):
	c=x.count(x[i])
	t[x[i]]=c

	
>>> print(t)
{1: 3, 2: 6, 4: 1, 5: 2, 3: 2, 7: 2, 6: 2, 8: 1, 9: 2}
>>> for i,j in heapq.nlargest(3,t.items(),key=itemgetter(1)):
	print(i,j)

	
2 6
1 3
5 2
>>> for i,j in heapq.nlargest(3,t.items(),key=itemgetter(0)):
	print(i,j)

	
9 2
8 1
7 2
>>> for i,j in heapq.nlargest(3,t.items(),key=itemgetter(-1)):
	print(i,j)

	
2 6
1 3
5 2
>>> import collections
>>> x=[[1,2,6],[1,3,4,5,7,8],[1,3,5,6,8,9],[2,5,7,11],[1,4,7,8,12]]
>>> d=collections.defaultdict(int)
>>> print(d)
defaultdict(<class 'int'>, {})
>>> print(type(d))
<class 'collections.defaultdict'>
>>> for i in x:
	for
	
SyntaxError: invalid syntax
>>> 
>>> l=[]
>>> for i in x:
	for j in i:
		l.append(j)

		
>>> print(l)
[1, 2, 6, 1, 3, 4, 5, 7, 8, 1, 3, 5, 6, 8, 9, 2, 5, 7, 11, 1, 4, 7, 8, 12]
>>> 