class badCoordinateException(Exception):
    pass
class field_object:
    def __init__(self, field_size):
        x_size, y_size = field_size
        self.__field__ = [["*" for j in range(y_size)] for i in range(x_size)]
        self.heighest_elem = [-1 for i in range(x_size)]
        self.heighest_free_cell = [0 for i in range(x_size)]

    def print(self):
        for i in self.__field__:
            print("   ".join(i))
            print("\n")
        print("___________________________________________________")

    def width(self):
        return len(self.__field__)

    def height(self):
        return len(self.__field__[0])

    def __getitem__(self,tup):
        x,y = tup
        return self.__field__[x][y]

    def __setitem__(self, tup, item):
        x,y = tup
        self.__field__[x][y] = item

    def available_moves(self):
        H = self.height()
        return [x for x in range(self.width()) if self.heighest_free_cell[x] < H]

    def make_move(self, x, move):
        y = self.heighest_free_cell[x]
        if y >= self.height():
            raise badCoordinateException(y)
        self[x,y] = move
        self.heighest_free_cell[x] +=1
        self.heighest_elem[x] +=1

    def unmake_move(self, x):
        y = self.heighest_elem[x]
        self[x,y] = "*"
        self.heighest_elem[x] -=1
        self.heighest_free_cell[x] -=1
