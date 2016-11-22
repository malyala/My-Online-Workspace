#include <iostream>
#include <ios>
#include <string>
#include <iomanip>

using std::cin;
using std::cout;
using std::endl;
using std::setprecision;
using std::string;
using std::streamsize;

int main(){
	cout << "name: ";
	string name;
	cin >> name;

	cout << "Midterm and final grades: ";
	double midterm, finale;
	cin >> midterm >> finale;

	cout << "Enter all hw grades, then EOF";
	int count = 0;
	double sum = 0;
	double x;

	while(cin >> x){
		count++;
		sum += x;
	}
	streamsize prec = cout.precision();
	cout << "Grade is " << setprecision(3)
	<< (0.2 * midterm) + (0.4 * finale) + (0.4 * (sum / count))
	<< setprecision(prec) << endl;
	return 0;
}
