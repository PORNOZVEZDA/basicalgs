class badCoordinateException(Exception):
    pass
class field_object:
    def __init__(self, field_size):
        x_size, y_size = field_size
        self.__field__ = [["*" for j in range(y_size)] for i in range(x_size)]
        self.heighest_elem = [-1 for i in range(x_size)]
        self.heighest_free_cell = [0 for i in range(x_size)]
        self.Width = x_size
        self.Height = y_size

    def print(self):
        for i in self.__field__:
            print("   ".join(i))
            print("\n")
        print("___________________________________________________")

    def width(self):
        return self.Width

    def height(self):
        return self.Height

    def __getitem__(self,tup):
        x,y = tup
        return self.__field__[x][y]

    def __setitem__(self, tup, item):
        x,y = tup
        self.__field__[x][y] = item

    def available_moves(self):
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

    def __valid_coord__(self, coord):
        x,y = coord
        if x < 0 or x >= self.Width:
            return false
        if y < 0 or y >= self.Height:
            return false
        return true

    def __create_neighbours_list__(self, coord, coord_vector):
        res = [coord]
        x,y = coord
        for delta_x, delta_y in coord_vector:
            x += delta_x
            y += delta_y
            if(self.__valid_coord__((x,y))):
                res.append((x,y))
            else:
                return res
        return res

    def __generate_potential_coord_lists__(self, point):
        potential_coords = []
        x,y = point
        deltas_list = [
                [(1,1),(1,1)],    ## / up
                [(-1,-1),(-1,-1)],## /down
                [(1,0),(1,0)], ## right
                [(-1,0),(-1,0)], ## left
                [(0,1),(0,1)], ## up
                [(0,-1),(0,-1)], ## down
                [(1,-1),(1,-1)], ## \ down
                [(-1,1),(-1,1)] ## \ up
                ]
        for vector in deltas_list:
            potential_list = self.__create_neighbours_list__(point, vector)
            if len(potential_list) > 1:
                potential_coords.append(potential_list)

    #TODO: implementation
    def count_successfull_combinations(self, list_of_combinations, turn):
        return 42

    #TODO: add function that finds all elements that can create combintation. i.e. 'wall' elements and elems that have diognal above them!
    def __count_combinations__(self, turn):
        global_res = 0
        heighest_elems_coords = [i for i in range(self.Width) if self.heighest_elem[x] != -1 and self.heighest_elem[x] < H]
        my_points = [(x,self.heighest_elem[x]) for x in heighest_elems_coords if self.heighest_elem[x] == turn]
        for point in my_cells:
            point_combination_list = self.__generate_potential_coord_lists__(point)
            point_value = self.count_successfull_combinations(point_combination_list, turn)
            global_res += point_value

    def evaluate(self, turn):
        pass

