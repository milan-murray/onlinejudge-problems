set = 0
for i in range(int(input().strip())):
	fit = True
	box = [int(j) for j in input().strip().split()]
	for measure in box:
		if measure > 20:
			fit = False
	set += 1
	if fit:
		print('Case', str(set) + ': good')
	else:
		print('Case', str(set) + ': bad')
