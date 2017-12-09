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


def checksum_part2(rows):
	sum = 0
	for row in rows:
		found = False
		srow = sorted(row)
		log.debug('sorted row: {}'.format(srow))
		for i in range(len(srow)):
			r_list = srow[i+1:]
			for j in r_list:
				log.debug('testing {} against {}'.format(srow[i], j))
				if evenly_divisible(srow[i], j):
					sum += j / srow[i]
					found = True
					break  # break to iterate over next row
			if found:
				break  # break to iterate over next row
	return sum




def parse_input(intext):
	inlist = []
	for textrow in intext.split('\n'):
		if textrow:
			numbers = [int(n) for n in textrow.split('\t')]
			inlist.append(numbers)
	return inlist


def evenly_divisible(a, b):
	return not b % a


def main():
	inlist = parse_input(common.read_input(2))
	print('The answer to part 1 is: {}'.format(checksum(inlist)))
	print('The answer to part 2 is: {}'.format(checksum_part2(inlist)))


if __name__ == '__main__':
	log = common.get_logger('day02', level='INFO')
	main()
