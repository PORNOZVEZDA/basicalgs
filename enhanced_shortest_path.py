from shortest_path import match_f
from shortest_path import indel_f
from enum import Enum
from sys import  argv

class A(Enum):
    M = 1
    R = 2
    D = 3
    I = 4

class cell:
    def __init__(self, cost, act):
        self.cost = cost
        self.action = act
    def __str__(self):
        return " cost: " + str(self.cost) 
    def __full_repr__(self):
        return " " + str(self.cost) + " " + str(self.action)

class field:
    def __init__(self, s, t):
        ''' in this class all actions take place on a row. (insert means insert in a row, delete means delete from row. '''
        self.col = " " + s
        self.row = " " + t
        self.__field__ = [[cell(0, A.M) for j in range(len(self.col))] for i in range(len(self.row))]
        # two initializations for comparison of empty string with non-empty string:
        # shortest path between empty string and n-symbols-string is n insertions (or deletions)
        for i in range(len(self.col)):
            self.__field__[0][i] = cell(i, A.I)
        for i in range(len(self.row)):
            self.__field__[i][0] = cell(i, A.D)
        #imagine that we prepend empty charecter in front of 
        # strings

    def __str__(self):
        return "".join(["".join([str(i) for i in j]) + "\n" for j in self.__field__])
    def __full_repr__(self):
        return "".join(["".join([i.__full_repr__() for i in j]) + "\n" for j in self.__field__])
        

    def __getitem__(self, tup):
        x,y = tup
        return self.__field__[x][y]
    def __setitem__(self, tup, value):
        x,y = tup
        self.__field__[x][y] = value

    def goal_cell(self):
        ''' return indeces of goal cell '''
        return (len(self.__field__) - 1, len(self.__field__[0]) - 1)

def shortest(f):
    ''' row is row, col is solumn.
    in this function we are trying to transform "t" to "s" in shortest way.
    index "i" is for 
    '''
    for i in range(1, len(f.row)):
        for j in range(1, len(f.col)):
            # we are searching for i,j 'th value!
            match = (f[(i-1, j-1)].cost + match_f(f.row[i], f.col[j]), A.M if f.row[i] == f.col[j] else A.R)
            # insert means insert in a row
            insert = (f[(i, j-1)].cost + indel_f(f.col[j]), A.I)
            delete = (f[(i-1, j)].cost + indel_f(f.row[i]), A.D)
            lowest_cost = min(match, insert, delete, key=lambda x: x[0])
            f[(i,j)] = cell(lowest_cost[0],lowest_cost[1]) 

def reconstruct_path(f, i, j, answer):
    if i == 0:
        answer += [A.I]*j
        return
    elif j == 0:
        answer += [A.D]*i
        return
    cur_action = f[i,j].action 
    answer += [cur_action]
    if(cur_action == A.M or cur_action == A.R):
        reconstruct_path(f, i-1, j-1, answer)
    if(cur_action == A.I):
        reconstruct_path(f, i, j-1, answer)
    if(cur_action == A.D):
        reconstruct_path(f, i-1, j, answer)


#TODO: reconstruct_path not working properly. Look at field.__init__ function.
# may be add 1 to length. 
if __name__ == '__main__':
    if len(argv) == 3:
        s,t = argv[1], argv[2]
    else:
        s, t = "helpewwr", "ahelpera"
    print("shortest path between \n" + s + "\n" + t + "\n:")
    f = field(s, t)
    shortest(f)
    print(f)
    print(f.__full_repr__())
    i, j = f.goal_cell()
    print("table path: " + str(f[i,j]))
    answer = []
    reconstruct_path(f, i, j, answer)
    print(answer)
    for i in answer:
            print(i)
    
