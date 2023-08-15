# Outline
- Prime factorisation of m
	- List of pairs of integers
		- The first is the number, second is the number of occurences
		- If the number of occurances is greater than the number, m divides n
	
## Sample Input
	6 9
	6 27
	20 10000
	20 100000
	1000 1009

## Sample Output
	9 divides 6!
	27 does not divide 6!
	10000 divides 20!
	100000 does not divide 20!
	1009 does not divide 1000!
	
## Sample Code
	for(auto it=pf.begin(); it != pf.end(); it++) {
		p = it->first; e = it->second;
		for(int x = p; x <= n && e > 0; x+= p) {
			while(x>1 &de>0) {
				--e;
				x /= p;
			}
		}
		if (e > 0) return false;
	}
	return true;
