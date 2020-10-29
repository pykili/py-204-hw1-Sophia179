a=input()
b=int(len(a))
phr=''
for i in range(b):
	if a[i]==' ':
		pass
	else:
		phr=phr+a[i]
c=int(len(phr))
for i in range(c):
	if phr[i]!=phr[c-1-i]:
		is_palindrom=not(phr[i]!=phr[c-1-i])
		break
	else:
		is_palindrom=not(phr[i]!=phr[c-1-i])
print(is_palindrom)
