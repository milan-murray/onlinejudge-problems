# Milan Murray
# Wednesday 23 Mar 2022
# 10082 WERTYU

if __name__ == '__main__':
	
	letters = "QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./`1234567890-="
	
	try:
		q_phrase = input().upper()
	except:
		q_phrase = ""
	while q_phrase != '':
		output = ""
		for letter in q_phrase:
			if letter != ' ':
				letter_not_found = True
				index = 1
				while letter_not_found:
					if letter == letters[index]:
						output += letters[index - 1]
						letter_not_found = False
					else:
						index += 1
			else:
				output += ' '
		print(output)
		try:
			q_phrase = input().upper()
		except:
			q_phrase = ""
