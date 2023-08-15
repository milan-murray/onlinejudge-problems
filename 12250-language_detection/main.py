ca_no = 1
while True:
	try:
		word = input().strip()
		if word == '#':
			break
		LANGUAGES = ['ENGLISH', 'SPANISH', 'GERMAN', 'FRENCH', 'ITALIAN', 'RUSSIAN']
		WORDS = ['HELLO', 'HOLA', 'HALLO', 'BONJOUR', 'CIAO', 'ZDRAVSTVUJTE']
		
		if word in WORDS:
			print('Case', str(ca_no) + ':', LANGUAGES[WORDS.index(word)])
		else:
			print('Case', str(ca_no) + ': UNKNOWN')
		ca_no += 1
	except:
		break
