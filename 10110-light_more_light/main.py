# Milan Murray
# Monday 28 Feb 22
# 10110 Light, more light


if __name__ == '__main__':
	# Imports
	from math import sqrt
	
	# Input & Processing & Output
	lights = int(input().strip())
	while lights != 0:
		if lights == (int(sqrt(lights))) * int((sqrt(lights))):
			print("yes")
		else:
			print("no")
		lights = int(input().strip())
