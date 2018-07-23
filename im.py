class field_object:
    def __init__(self, field_size):
        x_size, y_size = field_size
        self.__field__ = [["*" for j in range(y_size)] for i in range(x_size)]

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
