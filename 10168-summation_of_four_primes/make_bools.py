bools = []
for i in range(10000000):
	test_num = i + 1
	if test_num % 2 == 0 and test_num % 3:
		bools.append(False)
	else:
		bools.append(True)

