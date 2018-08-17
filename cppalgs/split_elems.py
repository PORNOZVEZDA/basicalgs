import sys

def count_sum(array, first, last):
    ''' sum of element from first to last including'''
    return sum(array[first:last])

def compute_split(multi, remaining_delimiters):
    last_elem_index = len(multi) - 1
    glob_table = [[None for i in range(last_elem_index+1)] for j in range(remaining_delimiters)]
    smallest_val = smallest_multiplicity(multi, last_elem_index, remaining_delimiters, glob_table)
    for i in glob_table:
        print(i)
    return smallest_val

class table_helper:
    def __init__(self, g_table, elem):
        self.global_table = g_table
        self.last_index, self.delimiters = elem
    def __call__(self, elem):
        self.global_table[self.delimiters-1][self.last_index] = elem

    def cash_exist(self):
        return self.global_table[self.delimiters-1][self.last_index] != None

    def return_cash(self):
        return self.global_table[self.delimiters-1][self.last_index][0]

def smallest_multiplicity(multi, last_elem_index, remaining_delimiters, global_table):
    t = table_helper(global_table, (last_elem_index, remaining_delimiters))

    if t.cash_exist():
        return t.return_cash()

    #edge 
    if remaining_delimiters == 0:
        t((count_sum(multi, 0, last_elem_index),0))
        return t.return_cash()

    if last_elem_index == 0:
        t((multi[0], 0))
        return t.return_cash()

    sums_array = [0 for i in range(last_elem_index)]
    for i in range(0, last_elem_index)[::-1]:
        #last_elem_index+1 to counte multi[last_elem_index] too!
        rhs_sum = count_sum(multi, i+1, last_elem_index+1)
        lhs_sum = smallest_multiplicity(multi, i, remaining_delimiters-1, global_table) 
        sums_array[i] = max(rhs_sum, lhs_sum)
    print(sums_array)
    print("delimiter: " + str(sums_array.index(min(sums_array))), end=" ")
    t((min(sums_array), sums_array.index(min(sums_array))))
    return t.return_cash()

if __name__ == '__main__':
    #delims = sys.argv[1]
    delims=3
    multiplicity = [1,3,8,9,10, 13, 18, 27, 30]
    smallest_sum = compute_split(multiplicity, delims)
    print("smallest_sum: " + str(smallest_sum))
