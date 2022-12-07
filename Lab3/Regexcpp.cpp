#include <iostream>
#include <regex>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
	setlocale(LC_ALL, "Russian");
	ifstream f("HTMLCode.txt");
	string str;
	smatch match;

	const auto r = regex(R"(<a.+?href=".+?"(.+?>|>).+?<\/a>)");
	while (getline(f, str))
	{
		regex_search(str, match, r);
		if (match.empty()) continue;
		cout << match[0] << "\n\n";
	}
}