for i in range(int(input().strip())):
	nums = [int(i) for i in input().strip().split()]
	if nums[0] > nums[1]:
		print('>')
	elif nums[1] > nums[0]:
		print('<')
	else:
		print('=')
