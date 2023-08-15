M_ONE = 567
D_TWO = 9
A_THREE = 7492
M_FOUR = 235
D_FIVE = 47
S_SIX = 498

for t in range(int(input().strip())):
	n = int(input().strip())
	
	n *= M_ONE
	n /= D_TWO
	n += A_THREE
	n *= M_FOUR
	n /= D_FIVE
	n -= S_SIX
	
	print(str(int(n))[-2])
	