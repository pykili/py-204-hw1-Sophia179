alphabet='abcdefghijklmnopqrstuvwxyz'
word=input()
for i in range(26):
	if alphabet[i] in word:
		print(alphabet[i])
