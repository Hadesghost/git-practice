from functools import reduce
def str2float(s):
	def f(x,y):
		return x*10+y
	def char2num(s):
		return ord(s)-ord('0')
	s1,s2=s.split('.')
	return reduce(f,map(char2num,s1))+(reduce(f,map(char2num,s2))/pow(10,len(s2)))

print('str2float(\'123.456\') =', str2float('123.456'))