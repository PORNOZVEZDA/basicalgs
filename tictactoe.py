from im import field_object
from random import randint
def process_field(field, turn, depth, max_depth):
    if depth == max_depth:
        field.print()
        return evaluate_field(field)
    moves = list_reasonable_moves(field, depth)
    results = []
    for i in moves:
        make_move(field, i, turn)
        results.append(process_field(field, opponent_turn(turn), depth+1, max_depth))
        unmake_move(field, i)
    return max(results)

def evaluate_field(field):
    return 1

def list_moves(field):
    return [i for i in range(field.width()) if find_y(field, i) != -1]

def list_reasonable_moves(field, depth):
    if depth < 2:
        return [field.width()//2]
    moves = list_moves(field)
    return [i for i in moves if is_surrounded(field, i)]

def find_y(field, x):
    '''
    return y coordinate of empty cell in column
    '''
    return find_elem_in_column(field, x, lambda x: x == "*")

def find_existing_y(field, x):
    '''
    return y coordinate of the heighest elem in column, if no elems in column, return -1
    '''
    if field[x,0] == "*":
        return -1
    for y in range(field.height()):
        if field[x,y] != "*":
            continue
        return y - 1
    return field.height() - 1

def find_elem_in_column(field, x, pred):
    for y in range(field.height()):
        if pred(field[x,y]):
            return y
    return -1

def opponent_turn(cur_turn):
    return "O" if cur_turn == "X" else "X"

def is_surrounded(field, x):
    coords = [i for i in  [x-1, x, x+1] if (i >= 0) and (i < field.width())]
    for i in coords:
        if find_existing_y(field, i) != -1:
            return True
    return False


def make_move(field, x, move):
    y = find_y(field, x)
    field[x,y] = move

def unmake_move(field, x):
    y = find_existing_y(field, x)
    field[x,y] = "*"

if __name__ == '__main__':
    #field = [["*" for j in range(10)] for i in range(6)]
    a = field_object((10,6))
    process_field(a , "O", 1, 8) 
#make_move(field, 2, "X")
#make_move(field, 2, "X")
#make_move(field, 2, "X")
#make_move(field, 3, "X")
#make_move(field, 4, "X")
#make_move(field, 3, "O")
#make_move(field, 3, "O")
#make_move(field, 3, "O")
#make_move(field, 4, "O")
#make_move(field, 4, "O")
#print_field(field)

