def normalize(name):
	if(name[0]>'Z'):
		b=chr(ord(name[0])-(ord('a')-ord('A')))
	else:
		b=name[0]
	for i in range(1,len(name)):
		if(name[i]<'a'):
			b=b+chr(ord(name[i])+(ord('a')-ord('A')))
		else:
			b=b+name[i]
	return b

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
		