s = 0
while True:
	text = input().strip().lower()
	if text == '*':
		break
	s += 1
	if text[0] == 'h':
		print('Case', str(s) + ': Hajj-e-Akbar')
	else:
		print('Case', str(s) + ': Hajj-e-Asghar')
