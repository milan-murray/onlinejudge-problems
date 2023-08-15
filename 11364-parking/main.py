from statistics import mean

for i in range(int(input().strip())):
	input()
	stores = [int(i) for i in input().strip().split()]
	l = len(stores)
	distance = 0
	
	if l == 1:
		print('0')
	elif l == 2:
		val = abs(stores[0] - stores[1])
		if val == 0:
			print('0')
		elif val == 1:
			print('2')
		else:
			distance += abs(min(stores) - max(stores)) * 2
			
			print(distance)
	else:
		m = int(mean(stores))
		distance += abs(m - min(stores)) * 2
		distance += abs(m - max(stores)) * 2
		
		print(distance)
			
