# Milan Murray
# Wednesday 30 Mar 22
# 10038 Jolly Jumpers

if __name__ == '__main__':
	while True:
		try:
			case_q = [int(i) for i in input().strip().split()]
			if not case_q:
				break
		except:
			break
		"""
		set = []
		n = len(case_q) - 1
		for i in range(n):
			set.append(i + 1)
		
		for i in range(n):
			a = case_q[i]
			b = case_q[i + 1]
			
			diff = abs(a - b)
			if diff in set:
				set.pop(set.index(diff))
		
		if set:
			print("Not jolly")
		else:
			print("Jolly")
		
		"""
		jolly_length = len(case_q)
		jolly = True
		if jolly_length != 1:
			second_diff = []
			for i in range(jolly_length - 1):
				second_diff.append(abs(case_q[i] - case_q[i + 1]))
				
			if min(second_diff) < 1 or max(second_diff) > jolly_length - 1:
				jolly = False
			
			# jolly_check = [i + 1 for i in range(len(second_diff))]
			
			# for number in jolly_check:
			# 	if number not in second_diff:
			# 		jolly = False
		
		if jolly:
			print("Jolly")
		else:
			print("Not jolly")
