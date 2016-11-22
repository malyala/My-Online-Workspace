#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::string;
using std::endl;
int main(){
	cout << "Enter name: ";
	string name;
	cin >> name;
	cout << endl;

	const string greeting = "Hello, " + name + "!";
	const int pad = 1;
	const int rows = (2 * pad) + 3;
	const string::size_type cols = greeting.size() + (pad * 2) + 2;

	for(int r = 0;r != rows; ++r){
		string::size_type c = 0;
		while(c != cols){
			if(c == (pad + 1) && r == (pad + 1)){
				cout << greeting;
				c += greeting.size();
			}else if(c==0 || c==(cols - 1) ||
					r==0 || r==(rows - 1)){
				cout << "*";
				c++;
			}else{
				cout << " ";
				c++;
			}
		}
		cout << endl;
	}
}
