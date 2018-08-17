import sys

def count_sum(array, first, last):
    ''' sum of element from first to last including'''
    return sum(array[first:last])

def smallest_multiplicity(multi, last_elem_index, remaining_delimiters):

    #edge 
    if remaining_delimiters == 0:
        return count_sum(multi, 0, last_elem_index)

    if last_elem_index == 0:
        return multi[0]

    sums_array = [0 for i in range(last_elem_index)]
    for i in range(0, last_elem_index)[::-1]:
        #last_elem_index+1 to counte multi[last_elem_index] too!
        rhs_sum = count_sum(multi, i+1, last_elem_index+1)
        lhs_sum = smallest_multiplicity(multi, i, remaining_delimiters-1) 
        sums_array[i] = max(rhs_sum, lhs_sum)
    print(sums_array)
    print("delimiter: " + str(sums_array.index(min(sums_array))), end=" ")
    return min(sums_array)

if __name__ == '__main__':
    #delims = sys.argv[1]
    delims=3
    multiplicity = [1,3,8,9,10, 13, 18, 27, 30]
    smallest_sum = smallest_multiplicity(multiplicity, len(multiplicity)-1, delims)
    print("smallest_sum: " + str(smallest_sum))
