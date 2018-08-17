#include <iostream>
#include <vector>
#include <string.h>
#include <numeric>
#include <algorithm>

using std::string;
using std::vector;
using v_it = vector<int>::iterator;
using std::cout;

int cost_of_splitting(const vector<int> & arr, size_t start, size_t stop){
	int result = std::accumulate(arr.begin() + start, 
					arr.begin() + stop + 1,
					0);
	return result;


}

int split_multiplicity(const vector<int> & mult, size_t cur_last_elem){
	//las_elem - 1, because split can not be after last elem.
	if(cur_last_elem == 1){
		return std::min(mult[0], mult[1]);
		cout << "reached end of recursion!\n";
				}
	for(size_t rhs_first_elem = cur_last_elem - 1; rhs_first_elem >= 0; rhs_first_elem--){
		size_t cur_cost = cost_of_splitting(mult, rhs_first_elem, cur_last_elem);
		size_t recur_cost = split_multiplicity(mult, rhs_first_elem);
		size_t minimal_index_cost = std::min(cur_cost, recur_cost);

	}


}

int main(int argc, char* argv[]){
	vector<int> testVector = {1, 3, 6, 6, 9, 13, 16, 16, 28, 29, 30, 31, 57};
	int smallest_sum = split_multiplicity(testVector, testVector.size() -1);
	std::cout << " smallest sum is:" + smallest_sum;

}
