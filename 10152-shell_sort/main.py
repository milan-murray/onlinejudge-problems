# Milan Murray
## Wednesday 23 Feb 22
## 10152 ShellSort

if __name__ == '__main__':
	# Input
	total_cases = int(input().strip())
	
	# For each case
	for case in range(total_cases):
		# Initialise
		original_turtles = []
		resulting_turtles = []
		resulting_indexs = []
		problem_index_not_found = True
		
		# Input Original and Resulting lists
		num_turtles = int(input().strip())
		for turtle in range(num_turtles):
			original_turtles.append(input().strip())
		for turtle in range(num_turtles):
			resulting_turtles.append(input().strip())
		
		# Processing
		if num_turtles > 1:
			inverse_index = -1
			# copy_original_turtles = original_turtles[:]
			for i in range(num_turtles):
				# this_turtle = copy_original_turtles.index(resulting_turtles[inverse_index])
				# copy_original_turtles[copy_original_turtles.index(resulting_turtles[inverse_index])] = ""
				# resulting_indexs.append(this_turtle)
				resulting_indexs.append(original_turtles.index(resulting_turtles[inverse_index]))
				inverse_index -= 1

			while len(resulting_indexs) > 1 and problem_index_not_found:
				if resulting_indexs[0] < resulting_indexs[1]:
					problem_index_not_found = False
				resulting_indexs.pop(0)
			
			# Output
			if len(resulting_indexs) > 1 or resulting_indexs[0] != 0:
				for index in resulting_indexs:
					print(original_turtles[index])
		print()
		# else:
		# 	print(original_turtles[0])
