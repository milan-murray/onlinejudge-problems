https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=13&page=show_problem&problem=1109

# Outline
- Input is int N (N <= 10,000,000)
- Generate an array of bools with size of N and check if each is prime or not
- Remember edge cases

## Sample Input
	24
	36
	46

## Sample Output
	3 11 3 7
	3 7 13 13
	11 11 17 7

### With 24
	24 / 4 = 6
	6 - 1 = 5 (Find prime)
	
		24 - 5 = 19
		
		(Odd) 19 -3 = 16
	
			16 | 3 | 13
			
				5 3 3 13
### With 36
	36 / 4 = 9
	
	9 - 1 = 8
	
	8 - 1 = 7
	
		36 - 7 = 29
		29 - 3 = 26
		
			7 3 3 23
		
