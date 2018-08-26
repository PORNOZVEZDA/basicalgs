from enum import Enum
from sys import argv

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Tile_color(Enum):
    white = 'w'
    red = 'r'
    brown = 'b'
    yellow = 'y'

class Tile:
    def __init__(self, m, n):
        self.tile_matrix = [[None for i in range(n)] for i in range(m)]
        self.last_empty_cell = (0, 0)
        self.positions = []
        self.Y = m
        self.X = n
        self.current_number = 0

    def valid_coords(self, x, y):
        if x >= self.X or y >= self.Y:
            return False
        if self.tile_matrix[y][x] != None:
            return False
        return True

    #TODO create method that calculates next cell to fulfill
    #how to change lastx|lasty cell after commiting move?
    def list_moves(self):
        res = []
        x, y = self.last_empty_cell
        if self.valid_coords(x+1, y):
            res += [[(x, y),(x+1, y)]]
        if self.valid_coords(x, y+1):
            res += [[(x,y),(x, y+1)]]
        return res

    def commit_move(self, x, y, x1, y1,color):
        self.commit_change(x, y, x1, y1, color)
        self.last_empty_cell = self.empty_cell()
        self.current_number += 1

    def uncommit_move(self, x, y, x1, y1):
        self.commit_change(x, y, x1, y1, None)
        self.last_empty_cell = min(x, x1), min(y, y1)
        self.current_number -= 1

    def empty_cell(self):
        for n,i in enumerate(self.tile_matrix):
            if None in i:
                return i.index(None), n
        return(-1, -1)

    def __str__(self):
        res = ""
        for i in self.tile_matrix:
            cur = " ".join(["{0:02}".format(j) for j in i]) + "\n"
            res += cur
        return res
    def commit_change(self, x, y, x1, y1, tile):
        self.tile_matrix[y][x] = tile
        self.tile_matrix[y1][x1] = tile

    def evaluate(self, empty_cells):
        if empty_cells == 0:
            #self.positions += [self.tile_matrix[:]]
            print(self)
            #print(self.last_empty_cell)
            return
        moves = self.list_moves()
        for move in moves:
            x,y = move[0][0],move[0][1]
            x1,y1 = move[1][0],move[1][1]

            self.commit_move(x,y,x1,y1,self.current_number)
            self.evaluate(empty_cells-2)
            self.uncommit_move(x,y,x1,y1)
            
if __name__ == '__main__':
    size = int(argv[1])
    desk = Tile(size,size)
    desk.evaluate(size*size)
    print(desk.positions)

