# Milan Murray
# 18 Feb 2022

# Constants
FASTEST_PERSON = 0
SECOND_FASTEST_PERSON = 1
SLOWEST_PERSON = -1
SECOND_SLOWEST_PERSON = -2

# Initialise
list_of_trials = []
trials_completed = 0

# Input number of trials
num_of_tirals = int(input().strip())

for i in range(num_of_tirals):
	list_of_people = []
	input()
	amount_of_people = int(input())
	# people_in = input().strip()

	for person in range(amount_of_people):
		people_in = input().strip()
		list_of_people.append(int(people_in))

	list_of_trials.append(list_of_people)
# print()

# Processing
for trial_of_people in list_of_trials:
	time_taken = 0
	cross_order = ''
	if trial_of_people:
		trial_of_people.sort()
		if len(trial_of_people) > 1:
			fastest_p = trial_of_people[FASTEST_PERSON]
			second_fastest_p = trial_of_people[SECOND_FASTEST_PERSON]

			while trial_of_people:
				if len(trial_of_people) == 3:
					time_taken += second_fastest_p + fastest_p + trial_of_people[SLOWEST_PERSON]
					cross_order += '\n' + str(trial_of_people[FASTEST_PERSON]) + ' ' + str(trial_of_people[SECOND_FASTEST_PERSON]) + '\n' + str(trial_of_people[FASTEST_PERSON]) + '\n' + str(trial_of_people[FASTEST_PERSON]) + ' ' + str(trial_of_people[-1])
					trial_of_people = []

				elif len(trial_of_people) == 2:
					time_taken += second_fastest_p
					cross_order += '\n' + str(trial_of_people[FASTEST_PERSON]) + ' ' + str(trial_of_people[SECOND_FASTEST_PERSON])
					trial_of_people = []

				else:
					method_a = 2 * fastest_p + trial_of_people[SLOWEST_PERSON] + trial_of_people[SECOND_SLOWEST_PERSON]
					method_b = 2 * second_fastest_p + fastest_p + trial_of_people[SLOWEST_PERSON]
					if method_a < method_b:
						time_taken += method_a
						cross_order += '\n' + str(trial_of_people[FASTEST_PERSON]) + ' ' + str(trial_of_people[SECOND_SLOWEST_PERSON]) + '\n' + str(trial_of_people[FASTEST_PERSON]) + '\n' + str(trial_of_people[FASTEST_PERSON]) + ' ' + str(trial_of_people[SLOWEST_PERSON]) + '\n' + str(trial_of_people[FASTEST_PERSON])

					else:
						time_taken += method_b
						cross_order += '\n' + str(trial_of_people[FASTEST_PERSON]) + ' ' + str(trial_of_people[SECOND_FASTEST_PERSON]) + '\n' + str(trial_of_people[FASTEST_PERSON]) + '\n' + str(trial_of_people[SECOND_SLOWEST_PERSON]) + ' ' + str(trial_of_people[SLOWEST_PERSON]) + '\n' + str(trial_of_people[SECOND_FASTEST_PERSON])

					trial_of_people.pop(-1)
					trial_of_people.pop(-1)
		else:
			time_taken += trial_of_people[FASTEST_PERSON]
			cross_order += '\n' + str(trial_of_people[FASTEST_PERSON])
	else:
		print(0)
	
	print(time_taken, end='')
	trials_completed += 1
	if trials_completed != num_of_tirals:
		print(cross_order, end='\n\n')
	else:
		print(cross_order)
	# print()
