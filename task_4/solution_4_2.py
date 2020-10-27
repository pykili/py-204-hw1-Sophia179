for j in range(10):
	a=input()
	b=int(len(a))
	form=str()
	lemma=str()
	k=0
	l=0
	m=0
	for x in range(b):
		if a[x]=='	':
			k=k+int(x)
			break
	for x in range(k+1,b):
		if a[x]=='	':
			l=l+int(x)
			break
	for x in range(l+1,b):
		if a[x]=='	':
			m=m+int(x)
			break
	for i in range(k+1,l):
		form=form+a[i]
	for i in range(l+1,m):
		lemma=lemma+a[i]
	c=int(len(form))
	d=int(len(lemma))
	if c>d:
		for i in range(d):
			if form[i]==lemma[i]:
				e=1
			else:
				e=0
	else:
		for i in range(c):
			if form[i]==lemma[i]:
				e=1
			else:
				e=0
	if e==1:
		print('они почти совпадают')
	else:
		print(form+' '+lemma)
