# Milan Murray
# Friday 04 Mar 22
# 10127 Ones

if __name__ == '__main__':
	number_in = input().strip()
	while number_in != "":
		number_in = int(number_in)
		
		number_one = 1
		count = 1
		while number_one%number_in != 0:
			number_one = (number_one*10+1)
			count += 1
			
		print(count)
		try:
			number_in = input().strip()
		except:
			break
