#include <iostream>
#include <vector>
#include <ctime>
#include <algorithm>

using namespace std;


void mergeSort(vector<int>& vec)
{
	if (vec.size() == 1) return;

	vector<int> vec1(vec.begin(), vec.begin() + vec.size() / 2);
	vector<int> vec2(vec.begin() + vec.size() / 2, vec.end());

	mergeSort(vec1);
	mergeSort(vec2);

	int lInd = 0, rInd = 0;

	for (int i = 0; i < vec.size(); i++)
	{
		if (lInd < vec1.size() && rInd < vec2.size())
		{
			if (vec1[lInd] < vec2[rInd])
			{
				vec[i] = vec1[lInd];
				lInd++;
			}
			else
			{
				vec[i] = vec2[rInd];
				rInd++;
			}
		}
		else if (lInd < vec1.size())
		{
			vec[i] = vec1[lInd];
			lInd++;
		}
		else
		{
			vec[i] = vec2[rInd];
			rInd++;
		}
	}

	return;
}


int main()
{
	vector<int> element;
	int random, n;
	cin >>random >> n;

	srand(random);
	for (int i = 0; i < n; i++)
	{
		element.push_back(rand() % 10000);
	}

	vector<int> stdSort = element;

	unsigned int mergeSt = clock();
	mergeSort(element);
	cout << "Merge sort time: " << clock() - mergeSt << "\n";

	unsigned int stdSortSt = clock();
	sort(stdSort.begin(), stdSort.end());
	cout << "Std sort time: " << clock() - stdSortSt;
}