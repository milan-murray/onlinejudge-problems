# Problem
- Some people on one side need to cross
- Max 2 at a time
- 1 must always return
- Everyone has different speeds
- Find the fast solution

# Sample Input
1

4
1
2
5
10

# Output
17		<!-- Total Seconds -->
1 2
1
5 10
2
1 2

# Strategy
- Order all the people
- Select the two fastest and two slowest A, B | C, D
	- See which solution is faster
		- AD ->
			- A <-
		- AC ->
			- A <-
		<!-- - AB -> -->

		- 2A + 1D + 1C
		- --- ---
		- AB ->
			- A <-
		- CD ->
			- B <-
		<!-- - AB -> -->

		- 1A + 2B + 1D

	- If 4 remain
		- The same

	- If 3 remain
		- AB ->
			- A <-
		- AC ->

	- If 2 remain
		- 2 go

	- If 1 remain
		- 1 go
