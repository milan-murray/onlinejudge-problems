num = 0
for i in range(int(input().strip())):
	salaries = [int(i) for i in input().strip().split()]
	salaries.sort()
	num+=1
	print('Case', str(num) + ':', salaries[1])
