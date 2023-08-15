#include <iostream>
#include <vector>

using namespace std;

constexpr int max_n = 2000000000;

vector<int> A;

// Declaration
void create_table();
int f(int n);

int main() {
	int n;
	
	create_table();

	while (cin >> n) {
		cout << f(n) << endl;
	}

	return 0;
}

// Definition
void create_table() {
	A.push_back(0);
	A.push_back(1);
	A.push_back(3);

	int fn = 3;
	int n = 5;
	int delta = 2;

	while (n <= max_n) {
		A.push_back(n);
		n += delta;
		if (A[delta] == fn) {
			delta++;
		}
		fn++;
	}
}

int f(int n) {
	int left = 0, right = A.size() - 1;
	int k;

	while (left <= right) {
		k = (left + right) / 2;

		if (A[k] == n) {
			return k;
		}
		else if (A[k] > n) {
			left = k + 1;
		}
		else {
			right = k - 1;
		}
	}
	while (k < A.size() && A[k] < n) {
		k++;
	}
}
