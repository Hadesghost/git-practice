from functools import reduce
def is_palindrome(n):
	s=str(n)
	for i in range(len(s)):
		if s[i]!=s[len(s)-1-i]: return False
	return True

output = filter(is_palindrome, range(1, 100000))
print(list(output))