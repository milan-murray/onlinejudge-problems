s = 0
for i in range(int(input().strip())):
	text = input().strip().lower()
	if text[0] == 'd':
		s += int(text.split()[-1])
	else:
		print(s)
