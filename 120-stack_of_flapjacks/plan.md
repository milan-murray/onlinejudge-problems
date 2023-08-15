# Stacks

- 1 2 3 4 5
	- Left to right, always increasing size

- 5 4 3 2 1
	- First number is bigger than last
	- 1 2 3 4 5

- 1 3 2 4 5
	- 1 5 4 2 3
		- 1 5 3 2 4
			- 4 2 3 5 1
				- 


- 5 2 4 3 1
	- First number is bigger than last
	- 1 3 4 2 5
		- 4 is greater than 2
		- 1 3 5 4 2
			- 4 is greater than 2
			- 1 3 5 2 4


# How it should be

- 5 1 2 3 4
	- 5 4 3 2 1
		- 1 2 3 4 5

## Analysis - Difference

- 5 1 2 3 4
-  4 1 1 1

- 4 2 1 5 3 | 4
-  2 1 -4 2
	- 4 2 1 3 5 | 1
	-  2 1 -2 -2
		- 5 3 1 2 4 | 2
		-  2 2 -1 -2
			- 5 4 2 1 3 | 3
			-  1 2 1 -2
				- 5 4 3 1 2 | 4
				-  1 1 2 -1
					- 5 4 3 2 1 | 0
					-  1 1 1 1
						- 1 2 3 4 5
						-  -1 -1 -1 -1
						
# Outline
	- Take the numbers with the largest difference between them
	- Identify the smaller of the two and filp on that one
	- Create a list at the beginning of pancake objects
			
