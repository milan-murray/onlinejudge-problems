# Milan Murray
# Wednesday 23 Feb 2022
# 846 Steps

from math import sqrt


if __name__ == '__main__':
	# Constants
	START_POS = 0
	END_POS = 1
	
	# Initialise
	all_cases = []
	
	# Input
	total_cases = int(input().strip())
	for case in range(total_cases):
		all_cases.append([int(i) for i in input().strip().split()])
	
	for case in all_cases:
		distance = case[END_POS] - case[START_POS]
		print(distance)
		print(sqrt(distance))
	
	print(all_cases)
