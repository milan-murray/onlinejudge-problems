// Milan
#include <iostream>

using namespace std;

// Declaration
void trim(char*);
bool isspace(char);

int main() {

	char* input;
	cin >> input;
	// cin.getline(input, 1024, '\n');
	// trim(input);
	// strcpy(candidate_names[i], input);

	trim(input);

	cout << input;

	return 0;
}

// Definition
void trim(char* str) {
	char* start = str;
	char* end;

	while (isspace(*start))
		start++;

	end = str;

	while (*end != '\0')
		end++;
	end--;
	while (end >= start && isspace(*end))
		end--;

	while (start <= end)
		*str++ = *start++;
	*str = '\0';
}

bool isspace(char char_in) {
	if (char_in == ' ')
		return 1;
	return 0;
}
