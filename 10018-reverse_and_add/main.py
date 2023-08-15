# Milan Murray
# Wednesday 06 Apr 22
# 10018 Reverse & Add
	
def check_palindrome(num_in):
	return num_in == num_in[::-1]

if __name__ == '__main__':
	for iterations in range(int(input().strip())):
		to_sub_one = False
		o_number = input().strip()
		r_number = o_number[::-1]
		# o_number += r_number
		int_num = str(int(o_number) + int(r_number))
		counter = 1
		
		while not check_palindrome(int_num):
			o_number = int_num
			r_number = o_number[::-1]
			int_num = str(int(o_number) + int(r_number))
			counter += 1
		
		print(counter, int_num)
