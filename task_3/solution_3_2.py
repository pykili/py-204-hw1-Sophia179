a=''
alphabet='abcdefghijklmnopqrstuvwxyz'
itog=''
for i in range(10):
	word=input()
	a=a+word
for i in range(26):
	if alphabet[i] in a:
		itog=itog+alphabet[i]
print(itog)
