https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=30&page=show_problem&problem=985

# 10044 Erdos Numbers
- Authors who jointly published with Erdos = 1
- Authors who publish with someone with 1 = 2
- And so on ...

## Input structure
- First line contains number of cases
- Next line contains ints P & N
	- P = Num of lines with paper descriptions
		- Eg. Smith, M.N., Martin, G., Erdos, P.: Newtonian forms of prime factors matrices
	- N = Num of lines with names

## Sample Input
	1
	4 3
	Smith, M.N., Martin, G., Erdos, P.: Newtonian forms of prime factor matrices
	Erdos, P., Reisig, W.: Stuttering in petri nets
	Smith, M.N., Chen, X.: First oder derivates in structured programming
	Jablonski, T., Hsueh, Z.: Selfstabilizing data structures
	Smith, M.N.
	Hsueh, Z.
	Chen, X.

## Sample Output
	Scenario 1
	Smith, M.N. 1
	Hsueh, Z. infinity
	Chen, X. 2
