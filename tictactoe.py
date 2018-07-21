from random import randint
def process_field(field, turn, depth, max_depth):
    if depth == max_depth:
        print_field(field)
        return evaluate_field(field)
    moves = list_moves(field)
    results = []
    for i in moves:
        make_move(field, i, turn)
        results.append(process_field(field, opponent_turn(turn), depth+1, max_depth))
        unmake_move(field, i)
    return max(results)

def evaluate_field(field):
    return 1

def print_field(field):
    for i in field:
        print("   ".join(i))
        print("\n")
    print("___________________________________________________")

def list_moves(field):
    return [i for i in range(len(field[0])) if find_y(field, i) != -1]

def list_reasonable_moves(field):
    moves = list_moves(field)
    return [i for i in moves if is_surrounded(field, i)]

def find_y(field, x):
    '''
    return y coordinate of empty cell in column
    '''
    return find_elem_in_column(field, x, lambda x: x == "*")

def find_existing_y(field, x):
    '''
    return y coordinate of heighest elem in column, if no elems in column, return -1
    '''
    if field[0][x] == "*":
        return -1
    for num, row in enumerate(field):
        if row[x] != "*":
            continue
        return num - 1
    return len(x) - 1
#    return find_elem_in_column(field, x, lambda x: x != "*")

def find_elem_in_column(field, x, pred):
    for num, row in enumerate(field):
        if pred(row[x]):
            return num
    return -1

def opponent_turn(cur_turn):
    return "O" if cur_turn == "X" else "X"

def is_surrounded(field, x):
    coords = [i in [x-1, x, x+1] if i >= 0 and i < len(field[0])]
    for i in coords:
        if find_existing_y(field, i) != -1:
            return True
    return False


def make_move(field, x, move):
    y = find_y(field, x)
    field[y][x] = move

def unmake_move(field, x):
    y = find_existing_y(field, x)
    field[y][x] = "*"

if __name__ == '__main__':
    field = [["*" for j in range(10)] for i in range(6)]
    process_field(field, "O", 1, 4) 
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

