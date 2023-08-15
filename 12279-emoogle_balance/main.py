case = 1
while True:
	try:
		if int(input().strip()) == 0:
			break
		nums = [int(i) for i in input().strip().split()]
		z_count = 0
		o_count = 0
		for num in nums:
			if num == 0:
				z_count += 1
			
		print("Case", str(case) + ":", len(nums) - (z_count*2))
		case += 1
				
	except:
		break
