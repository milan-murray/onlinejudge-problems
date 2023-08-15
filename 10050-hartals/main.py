# Milan Murray
# Sunday 03 Apr 22
# 10050 - Hartals

if __name__ == '__main__':

	# Input
	for t_cases in range(int(input().strip())):
		n_days = int(input().strip())
		h = []
		h_len = int(input().strip())
		for i in range(h_len):
			h.append(int(input().strip()))
		
		# Processing
		missed_days = 0
		for day in range(n_days):
			lcv = True
			h_index = 0
			# for h_number in h:
			while lcv or lcv:
				h_number = h[h_index]
				if (day + 1) % h_number == 0 and day % 7 < 5:
					missed_days += 1
					lcv = False
				h_index += 1
				if h_index >= h_len:
					lcv = False
		
		# Output
		print(missed_days)
					
		
		