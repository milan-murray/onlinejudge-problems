for i in range(int(input().strip())):
	word = input().strip().upper()
	if len(word) == 3:
		if word[0] == 'O' and word[1] == 'N':
			print('1')
		elif word[0] == 'O' and word[2] == 'E':
			print('1')
		elif word[1] == 'N' and word[2] == 'E':
			print('1')
		else:
			print('2')
	else:
		print('3')
