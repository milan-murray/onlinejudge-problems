<a>https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=32&page=show_problem&problem=1093</a>

# DEAL WITH DUPLICATE NAMES

# Strategy

- The first line of the input consists of a single integer K giving the number of test cases

- Compare position in original array to the desired array

- Turtles are in a starting stack
- They must be put in a new order
	- We can remove and place them in a certain order

## Sample input
	2
	3
	Yertle
	Duke of Earl
	Sir Lancelot
	Duke of Earl
	Yertle
	Sir Lancelot
	9
	Yertle
	Duke of Earl
	Sir Lancelot
	Elizabeth Windsor
	Michael Eisner
	Richard M. Nixon
	Mr. Rogers
	Ford Perfect
	Mack
	Yertle
	Richard M. Nixon
	Sir Lancelot
	Duke of Earl
	Elizabeth Windsor
	Michael Eisner
	Mr. Rogers
	Ford Perfect
	Mack

## Sample output
	Duke of Earl
	Sir Lancelot
	Richard M. Nixon
	Yertle

## Ideas
	1	1
	2	3
	3	2
	4	4
	5	5
