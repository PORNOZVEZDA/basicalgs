from im import field_object
from random import randint
def process_field(field, turn, depth, max_depth):
    if depth == max_depth:
        field.print()
        return evaluate_field(field)
    moves = list_reasonable_moves(field, depth)
    results = []
    for i in moves:
        field.make_move(i, turn)
        results.append(process_field(field, opponent_turn(turn), depth+1, max_depth))
        field.unmake_move(i)
    return max(results)

def evaluate_field(field):
    return 1

def list_moves(field):
    return field.available_moves()

def list_reasonable_moves(field, depth):
    if depth < 2:
        return [field.width()//2]
    moves = list_moves(field)
    return [i for i in moves if is_surrounded(field, i)]

def opponent_turn(cur_turn):
    return "O" if cur_turn == "X" else "X"

def is_surrounded(field, x):
    coords = [i for i in  [x-1, x, x+1] if (i >= 0) and (i < field.width())]
    for i in coords:
        if field.heighest_elem[i] != -1:
            return True
    return False


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

