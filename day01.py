import common

log = common.get_logger(__name__)


def matches_next(L, i, step=1):
	j = (i + step) % len(L)
	return L[i] == L[j]


def sum_matches(L):
	match_sum = 0
	for i in range(len(L)):
		if matches_next(L, i):
			match_sum += L[i]
	return match_sum


def sum_matches_part2(L):
	match_sum = 0
	for i in range(len(L)):
		step = len(L) / 2
		if matches_next(L, i, step=step):
			match_sum += L[i]
	return match_sum


def main():
	input = common.read_input(01)
	input_array = [int(c) for c in input]
	answer = sum_matches(input_array)
	answer2 = sum_matches_part2(input_array)
	print('The part 1 answer is: {}'.format(answer))
	print('The part 2 answer is: {}'.format(answer2))


if __name__ == '__main__':
	log = common.get_logger('day01')
	main()
