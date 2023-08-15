# Strategy

- Input consists of a line containing n, the number of test cases.

- Can each step is non-negative, and can differ from the prior step by no more than +- 1

- Output number of steps

- Not needed to precompute


## Sample Input
	3
	45 48
	45 49
	45 50

## Sample Output
	3
	3
	4

## Visual
	|---------------------------------------------------|
	| Distance	|Steps	|		Pattern					|
	|---------------------------------------------------|
	| 1 		|1		|	1							|
	| 2 		|2		|	1	1						|
	| 3 		|3		|	1	1	1					|
	| 4 		|3		|	1	2	1					|
	| 5 		|4		|	1	2	1	1				|
	| 6 		|4		|	1	2	2	1				|
	| 7 		|5		|	1	2	2	1	1			|
	| 8 		|5		|	1	2	2	2	1			|
	| 9 		|5		|	1	2	3	2	1			|
	| 10		|6		|	1	2	3	2	1	1		|
	| 11		|6		|	1	2	3	2	2	1		|
	| 12		|6		|	1	2	3	3	2	1		|
	| 13		|7		|	1	2	3	3	2	1	1	|
	| 14		|7		|	1	2	3	3	2	2	1	|
	| 15		|7		|	1	2	3	3	3	2	1	|
	| 16		|7		|	1	2	3	4	3	2	1	|
	| 17		|8		|	1	2	3	4	3	2	1 1	|
	|---------------------------------------------------|

## Ideas
- If the distance is odd the middle number is equal to the adjacent numbers
- Must start and end at 1

