

def parse(function_string):
	if (function_string.startswith('+')):
		def add(value):
			return value + int(function_string[1:])
		return add

	raise ValueError('Illegal function : %s' % function_string)