Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f1(x):
	for i in range(0,len(x)):
		for j in x[i]:
			print(j)

			
>>> m=[[1,2,3,4],[5,6,7,8],[2,30,0,2],[6,2,0,7]]
>>> f1(m)
1
2
3
4
5
6
7
8
2
30
0
2
6
2
0
7
>>> def f1(x):
	for i in range(0,len(x)):
		if i%2==0:
			for j in x[i]:
				print(j)
		else:
			for j in x[-i]
			
SyntaxError: invalid syntax
>>> def f1(x):
	for i in range(0,len(x)):
		if i%2==0:
			for j in x[i]:
				print(j)
		else:
			for j in x[-i]:
				print(j)

				
>>> m=[[1,2,3,4],[5,6,7,8],[2,5,0,2],[2,3,6,1]]
>>> f1(m)
1
2
3
4
2
3
6
1
2
5
0
2
5
6
7
8
>>> def f1(x):
	for i in range(0,len(x)):
		if i%2==0:
			for j in x[i]:
				print(j)
		else:
			for j in x[:-i]:
				print(j)

				
>>> m=[[1,2,3,4],[5,6,7,8],[2,3,0,2],[2,9,1,2]]
>>> f1(m)
1
2
3
4
[1, 2, 3, 4]
[5, 6, 7, 8]
[2, 3, 0, 2]
2
3
0
2
[1, 2, 3, 4]
>>> def f1(x):
	for i in range(0,len(x)):
		if i%2==0:
			for j in x[i]:
				print(j)
		else:
			for j in x[::-i]:
				print(j)

				
>>> m=[[1,2,3,4],[5,6,7,8],[2,3,0,1],[2,6,0,1]]
>>> f1(m)
1
2
3
4
[2, 6, 0, 1]
[2, 3, 0, 1]
[5, 6, 7, 8]
[1, 2, 3, 4]
2
3
0
1
[2, 6, 0, 1]
[1, 2, 3, 4]
>>> def f1(x):
	for i in range(0,len(x)):
		if i%2==0:
			for j in x[i]:
				print(j)
		else:
			for j in i[::-1]:
				print(j)

				
>>> m=[[1,2,3,4],[5,6,7,8],[2,3,0,2],[2,6,0,1]]
>>> f1(m)
1
2
3
4
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    f1(m)
  File "<pyshell#25>", line 7, in f1
    for j in i[::-1]:
TypeError: 'int' object is not subscriptable
>>> def f1(x):
	for i in range(0,len(x)):
		if i%2==0:
			for j in x[i]:
				print(j)
		else:
			for j in x[i][::-1]:
				print(j)

				
>>> m=[[1,2,3,4],[5,6,7,8],[2,3,0,2],[2,6,0,1]]
>>> f1(m)
1
2
3
4
8
7
6
5
2
3
0
2
1
0
6
2
>>> 