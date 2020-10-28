alphabet='abcdefghijklmnopqrstuvwxyz'
itog=''
word=input()
for i in range(26):
	if alphabet[i] in word:
		itog=itog+alphabet[i]
print(itog)
