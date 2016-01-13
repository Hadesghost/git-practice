import functools

def log(text=None):
	def decorator(func=None):
		print('begin call')
		@functools.wraps(func)
		def wrapper(*args, **kw):
			if not callable(text):
				print("%s %s()" % (text,func.__name__))
			else:
				print("call %s()" % func.__name__)
			r=func(*args, **kw)
			return r
		return wrapper
	if not callable(text):
		return decorator
	else:
		return decorator(text)


@log('execute')
def now():
	print("2016-1-13")

now()

@log
def now():
	print("2016-1-13")

now()