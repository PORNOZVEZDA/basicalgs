from sys import argv
def match_f(lhs, rhs):
    if lhs == rhs:
        return 0
    else:
        return 1
def indel_f(a):
    return 1


def string_compare(s, t, i, j, debug=False):
    global shared_variable
    shared_variable += 1  
    if debug:
        print("call num " + str(shared_variable))
    ''' s is main string, 
        t is additional string
    '''
    if i == 0:
        return j * indel_f(' ')
    if j == 0:
        return i * indel_f(' ')
    match = string_compare(s, t, i-1, j-1) + match_f(s[i], t[j])
    #insert means insert in additional string
    insert = string_compare(s, t, i, j-1) + indel_f(t[j])
    delete = string_compare(s, t, i-1, j) + indel_f(s[i])
    lowest_cost = min(match, insert, delete)
    return lowest_cost

if __name__ == '__main__':
    if len(argv) == 3:
        a, b = argv[1], argv[2]
    else:
        a, b = "hellap", "heaplaaaa"
    print("path between: \n" + a + "\n" + b)
    shared_variable = 0
    cost = string_compare(a,b,len(a)-1, len(b)-1)
    print(cost)
