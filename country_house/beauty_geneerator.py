from enum import Enum

class Tile_color(Enum):
    white = 'w'
    red = 'r'
    brown = 'b'
    yellow = 'y'

class Tile:
    def __init__(self, m, n):
        self.tile_matrix = [[None for i in range(n)] for i in range(m)]
        self.last_empty_cell = (0, 0)
        self.result = []
        self.Y = m
        self.X = n

    def valid_coords(self, x, y):
        if x >= self.X or y >= self.Y:
            return False
        if self.tile_matrix[y][x] != None:
            return False
        return True

    #TODO create method that calculates next cell to fulfill
    #how to change lastx|lasty cell after commiting move?
    def list_moves(self, lastx, lasty):
        res = []
        x, y = self.last_empty_cell
        if valid_coords(x+1, y):
            res += [[(x, y),(x+1, y)]]
        if valid_coords(x, y+1):
            res += [[(x,y),(x, y+1)]]
        return res

    def commit_move(self, x, y,x1, y1,color):
        self.commit_change(x, y, x1, y1, color)

    def uncommit_move(self, x, y, x1, y1):
        self.commit_change(x, y, x1, y1, None)

    def commit_change(self, x, y, x1, y1, color):
        self.tile_matrix[x][y] = color
        self.tile_matrix[x1][y1] = color

    def evaluate(self, empty_cells):
        if empty_cells == 0:

if __name__ == '__main__':
    desk = Tile(6, 6)

