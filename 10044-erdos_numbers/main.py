# Milan Murray
# Wednesday 02 Mar 22
# 10044 Erdos Numbers

class Node:
	def __init__(self, name):
		self.name = name
		self.number = -1
		self.adjacent_nodes = list()
		
	def connect_with(self, other):
		if not other.name in self.adjacent_nodes.keys():
			self.adjacent_nodes[other.name]
	
	def erdos_number(self):
		if self.number >= 0:
			pass

if __name__ == '__main__':
	# CONSTANTS
	PAPERS = 0
	NAMES = 1
	
	# Input total test cases
	cases = int(input().strip())
	
	for case in range(cases):
		# Initialise
		case_output = 'Scenario ' + str(case + 1) + '\n'
		case_conditions = [int(i) for i in input().strip().split()]
		d = dict()
		for i in range(case_conditions[PAPERS]):
			line = input().strip().split(sep=':')[0]
			parts = line.split(sep = ',')
			current_paper_author_list = list()
			for k in range(0, len(parts), 2):
				if k + 1 < len(parts):
					author_name = parts[k].strip() + ',' + parts[k+1]
				else:
					author_name = parts[k]
				current_paper_author_list.append(author_name)
			print(current_paper_author_list)
			current_paper_node_list = list()
			for author_name in current_paper_author_list:
				if not author_name in d.keys():
					d[author_name] = Node(author_name)
				current_paper_node_list.append(d[author_name])
			print(current_paper_node_list)

		# for i in range(case_conditions[NAMES]):
		
		print(case_output)
