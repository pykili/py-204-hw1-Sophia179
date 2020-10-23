a=input()
b=len(a)
x=0
for x in range(b+1):
	if a[x]>a[x+1]:
		print(a[x])
