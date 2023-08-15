// Milan
#include <iostream>
#include <vector>

using namespace std;

// Declaration
void trim(char*);
bool isspace(char);

int main() {
	char* runs = new char;
	cin >> runs;
	trim(runs);
	cout << runs << endl;

	cin.getline(runs, 1024, '\n');

	// Sort All the people

	// trim(input);
	// strcpy(candidate_names[i], input);

	return 0;
}

// Definition
void trim(char* str) {
	char* start = str;
	char* end;

	while (isspace(*start)) {
		start++;
	}

	end = str;

	while (*end != '\0') {
		end++;
	}

	end--;
	while (end >= start && isspace(*end)) {
		end--;
	}

	while (start <= end) {
		*str++ = *start++;
	}
	*str = '\0';
}

bool isspace(char char_in) {
	if (char_in == ' ')
		return 1;
	return 0;
}
