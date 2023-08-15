https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=13&page=show_problem&problem=1122

## Python is a no go

# 10181 Puzzle Problem

- 15 tiles
- Exchange tile with adjacent tile

- Given a random puzzle
	- Tiles move as
	- R L U D
		- R: right
		- U: up
		- ...
	- Each puzzle takes no more than 45 moves
		- Over 50 is illegal
			- Print ("This puzzle is not solvable.")
			
## Sample Input
	2
	2 3 4 0
	1 5 7 8
	9 6 10 12
	13 14 11 15
	13 1 2 4
	5 0 3 7
	9 6 10 12
	15 8 11 14

## Sample Output
	LLLDRDRDR
	This puzzle is not solvable.

### Theory
- First move can be any move
	- C0
		- U	C1
			- R	C5
			- L	C6
			- D	C7
		- R	C2
			- R
			- U
			- D
		- L	C3
			- L
			- U
			- D
		- D	C4
			- R
			- D
			- L
- If we had just moved Up, it makes no sence to down next

1. Check if solvable
2. Hash table or map to keep the already visited configurations
3. He... to decide which branch worths to be explored first
4. Define a threshold to be updated progresively to apply IDA* strategy

- Note the movements made so far
- The movements that could be made next

- f = count of movemnts
- g = An estimation of pending steps
	- h = alpha * f + beta * g

# Visual
	2	3	4	
	11	5	7	8
	9	6	10	12
	13	14	1	15
	
- 1D array = [2, 3, 4, 5, 1, 5, 7, 8, 9, 6, 10, 12, 13, 14, 11, 15]
	- G = The distance of each tile to its correct destination
		- Sum of i=0; i <= 15; manhaton(curr_pos, true_pos)
		
# Look up manhaton distance
