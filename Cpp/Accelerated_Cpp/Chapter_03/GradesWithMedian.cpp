#include <iostream>
#include <ios>
#include <string>
#include <iomanip>
#include <algorithm>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::setprecision;
using std::string;
using std::streamsize;
using std::vector;

int main(){
	cout << "name: ";
	string name;
	cin >> name;

	cout << "Midterm and final grades: ";
	double midterm, finale;
	cin >> midterm >> finale;

	cout << "Enter all hw grades, then EOF";
	vector<double> hw;
	double x;

	while(cin >> x){
		hw.push_back(x);
	}
	sort(hw.begin(), hw.end());

	typedef vector<double>::size_type vec_sz;
	vec_sz hwSize = hw.size();
	if(hwSize == 0){
		cout << "Need some hw grades. Try again." << endl;
		return 1;
	}
	vec_sz mid = hwSize / 2;
	double median = (hwSize % 2) == 0 ? (hw[mid] + hw[mid - 1]) / 2 : hw[mid];


	streamsize prec = cout.precision();
	cout << "Grade is " << setprecision(3)
	<< (0.2 * midterm) + (0.4 * finale) + (0.4 * median)
	<< setprecision(prec) << endl;
	return 0;
}
