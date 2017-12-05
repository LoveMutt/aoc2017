import common

log = common.get_logger(__name__)


def matches_next(L, i):
	j = (i + 1) % len(L)
	return L[i] == L[j]


def sum_matches(L):
	sum = 0
	for i in range(len(L)):
		if matches_next(L, i):
			sum += L[i]
	return sum

def main():
	input = common.read_input(01)
	input_array = [int(c) for c in input]
	answer = sum_matches(input_array)
	print('The answer is: {}'.format(answer))


if __name__ == '__main__':
	log = common.get_logger('day01')
	main()
