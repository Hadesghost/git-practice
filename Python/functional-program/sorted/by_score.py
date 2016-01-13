def by_name(t):
	return (t[1],t[0].lower())

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name,reverse = True)
print(L2)