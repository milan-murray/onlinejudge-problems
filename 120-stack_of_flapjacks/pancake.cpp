// Milan Murray

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	string user_input;
	vector<int> nums{};
	size_t pos = 0;
	
	cin >> user_input;
	// input
	while((pos = user_input.find(" ")) != string::npos) {
		nums.push_back(stoi((user_input.substr(0, pos))));
		user_input.erase(0, pos + 1);
	}	
	
	for (int i = 0; i < sizeof(nums); i++) {
		cout << nums[i];
	}
	
	// Processing
	
	
	
	
	
	// Output

	return 0;
}
