# Milan Murray
# Saturday 2 Apr 22
# 10035 Primary Arithmetic

if __name__ == '__main__':
	while True:
		try:
			numbers_in = input().strip().split()
			if not numbers_in:
				break
			if numbers_in[0] == '0' and numbers_in[1] == '0':
				break
			
		except:
			break

		if int(numbers_in[0]) > int(numbers_in[1]):
			temp_num = numbers_in[0]
			numbers_in[0] = numbers_in[1]
			numbers_in[1] = temp_num
		# print(numbers_in)
		
		carry = 0
		just_carried = False
		for i in range(len(numbers_in[0])):
			case_number = int(numbers_in[1][-i - 1]) + int(numbers_in[0][-i - 1])
			if case_number > 9:
				carry += 1
				just_carried = True
			else:
				if just_carried:
					if case_number + 1 > 9:
						carry += 1
						just_carried = True
					else:
						just_carried = False
		
		if just_carried:
			if len(numbers_in[1]) > len(numbers_in[0]):
				temp_index = -len(numbers_in[0])
				big_number = numbers_in[1][:temp_index]
				while just_carried and big_number:
					temp_index = -1
					if big_number[-1] == '9':
						carry += 1
						just_carried = True
						big_number = big_number[:-1]
					else:
						just_carried = False
		
		if carry > 0:
			if carry == 1:
				print("1 carry operation.")
			else:
				print(str(carry) + " carry operations.")
		else:
			print("No carry operation.")
