import common

log = common.get_logger(__name__)


def max_and_min(input):
	maxval = max(input)
	minval = min(input)
	return maxval, minval


def checksum(rows):
	sum = 0
	for row in rows:
		maxval, minval = max_and_min(row)
		sum += abs(maxval - minval)
	return sum


def parse_input(intext):
	inlist = []
	for textrow in intext.split('\n'):
		if textrow:
			numbers = [int(n) for n in textrow.split('\t')]
			inlist.append(numbers)
	return inlist


def main():
	inlist = parse_input(common.read_input(02))
	print('The answer is: {}'.format(checksum(inlist)))


if __name__ == '__main__':
	log = common.get_logger('day02')
	main()
