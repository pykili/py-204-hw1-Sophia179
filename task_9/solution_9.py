b=0
c=input('введите число от 0 до 100: ')
n=int(c)
a=n*n
print(a)
for i in range(2*n):
	if i % 2 == 1:
		b=b+i
print(b)
if a==b:
	print('true')
else:
	print('false')
