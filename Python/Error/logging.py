#err_logging.py

from logging import exception

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
	else:
		print('this is else')
	finally:
		print('this is finally which always be excuted if exist.')

main()
print('END')