# Milan Murray
# Wednesday 09 Mar 22
# 10160 Servicing stations

import enum
from sqlite3 import connect


if __name__ == '__main__':
	while True:
		try:
			detail = input().strip().split()
			num_towns = int(detail[0])
			num_towns_directly_connected = int(detail[1])
			town_info = list()
			for i in range(num_towns):
				town_info.append([])
			
			
			case = [int(i) for i in input().strip().split()]
			while case != [0, 0]:
				print(case)
				
				# if case[1] not in town_info[case[0] - 1]:
				town_info[case[0] - 1].append(case[1])
				town_info[case[1] - 1].append(case[0])
				
				
				case = [int(i) for i in input().strip().split()]
			
			print(town_info)
			connected_towns = list()
			most_connected_town = town_info[0]
			index_of_most_connected_town = 0
			for index, town in enumerate(town_info):
				if len(town) > len(most_connected_town):
					most_connected_town = town
					index_of_most_connected_town = index
			
			for towns_with_service in most_connected_town:
				connected_towns.append(towns_with_service)
			town_info.pop(index_of_most_connected_town)
			
			while len(towns_with_service) != num_towns:
				for index, town in enumerate(town_info):
					if len(town) > len(most_connected_town):
						most_connected_town = town
						index_of_most_connected_town = index
			
		except:
			break
	# for i in range(num_towns_directly_connected):
	# 	case = input().strip().split()
		
