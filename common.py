import logging



def get_logger(name, level='DEBUG'):
	logging.basicConfig(level=logging.__getattribute__(level))
	return logging.getLogger(name)


def read_input(day):
	fn = 'input_day{:02}.txt'.format(day)
	with open(fn) as f:
		return f.read()
