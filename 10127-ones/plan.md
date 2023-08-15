https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=13&page=show_problem&problem=1068

# 10127 Ones
- 0 <= N <= 10000
	- What is the lowest multiple of N to have only ONES in the answer

## Sample Input
	3
	7
	9901

## Sample Output
	3
	6
	12

## Ideas
	one_number = X . number_in
		X = one_number / number_in
		
		7
		14 + 1
		11 + 1 + 1
		
		3
		6
		9
		12
		15
		18
		21
		24
		27
		30
		33
		36
		39
		42
		45
		48
		51
		54
		57
		60
		...
		111
		
		7
		14		4
		21		11		1		1
		28
		35
		42
		49
		56
		63
		70
		77
		84
		91
		98
		105
		112
		119
		
- input_num * X = series_of_ones
- X = series_of_ones / input_nums
