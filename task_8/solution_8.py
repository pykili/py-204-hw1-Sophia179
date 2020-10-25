a=input()
b=int(a)
d=int(a)
f=1
for i in range(b):
	c=input()
	e=int(c)
	d=d+e
	f=f+1
	if e==0:
		break
print(d/f)
