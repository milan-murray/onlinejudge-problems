while True:
	try:
		var = int(input().strip())
		if var == 0:
			break
	except:
		break
	origin = [int(i) for i in input().strip().split()]
	for i in range(var):
		cords = [int(i) for i in input().strip().split()]
		if cords[0] == origin[0] or cords[1] == origin[1]:
			print('divisa')
		elif cords[0] > origin[0] and cords[1] > origin[1]:
			print('NE')
		elif cords[0] > origin[0] and cords[1] < origin[1]:
			print('SE')
		elif cords[0] < origin[0] and cords[1] > origin[1]:
			print('NO')
		else:
			print('SO')
     