# Package name : matrix position
# Author : Jinghao , LiuShuhua
#
# Description:
# 1. In the coordinate system, we define the direction of x as downward along the origin, and the direction of y as right along the origin.
# 2. We define the "length" of a matrix as how many rows the matrix has, and "length" is equivalent to "rows";
#               "Width" is defined as how many columns the matrix has, and "width" is equivalent to "columns".
#
# Our contact information = {Jinghao:psymhmch@163.com , LiuShuhua:492653598@qq.com} (:our emails can be stored by dictionary lol
# This project github : https://github.com/Zeaulo/matrix_position

from .urls import is_matrix, matrix_dict, direction_iter

#codes_key
class matrix():
    def __init__(self, matrix):
        is_matrix(matrix)
        self.matrix = matrix
        self.width = len(matrix[0]) ; self.columns = self.width
        self.length = len(matrix) ; self.rows = self.length
        self.shape = (self.length, self.width) ; self.size = self.shape
        self.matrix_dict = matrix_dict(matrix)
        self.now = {(0, 0) : self.matrix[0][0]}


    def show(self, quick = False):
        '''
        introduction:
        -
        Show the matrix what you input.

        parameters: (`quick=False`)
        -
        if `quick` = False (fault), it prints a value of the matrix every time, but will ensure that the entire matrix is aligned.

        if `quick` = True, it will prints one row of the matrix at a time.That's why it's fast.
        '''
        if quick:
            for i in self.matrix:
                print(i)
        else:
            max_len = 0
            for x in range(self.length):
                for y in range(self.width):
                    if max_len < len(str(self.matrix[x][y])):
                        max_len = len(str(self.matrix[x][y]))
            
            for x in range(self.length):
                for y in range(self.width):
                    print('{}'.format(self.matrix[x][y]).center(max_len+2), end='')
                print()


    def get_position(self, value, return_first_one = False):
        '''
        introduction:
        -
        input the value of the matrix, and return the value's position(coordinate) from the matrix.
        
        parameters: (`value`, `return_first_one=False`)
        -
        if `return_first_one`= False (fault), it return all coordinate from the matrix.

        if `return_first_one`= True, it will return the first coordinate from the matrix.
        '''
        if return_first_one:
            for x in range(self.length):
                for y in range(self.width):
                    if self.matrix[x][y] == value:
                        return (x, y)
        else:
            positions = []
            for x in range(self.length):
                for y in range(self.width):
                    if self.matrix[x][y] == value:
                        positions.append((x, y)) 
            return positions


    def get_value(self, position:tuple):
        '''
        introduction:
        -
        input position(coordinate) and return its value.
        
        parameters: (`position:tuple`)
        -
        Note: input's position need to be equal to the format of (x, y).
        '''
        return self.matrix[position[0]][position[1]]


    def fourD(self, position):
        '''
        introduction:
        -
        input position(coordinate) and return its surrounding positions and values including four directions.
        
        the order is ： ← ↑ ↓ →
        
        parameters: (`position`)
        -
        Note: input's position need to be equal to the format of (x, y).
        '''
        x = position[0]
        y = position[1]
        fourD_dict = {}
        for i, j in direction_iter(4):  # fourD_orders : ← ↑ ↓ →
            try:
                if x + i < 0 or y + j < 0:
                    fourD_dict[(x+i, y+j)] = None
                else:
                    fourD_dict[(x+i, y+j)] = self.matrix[x+i][y+j]
            except:
                fourD_dict[(x+i, y+j)] = None
        return fourD_dict


    def eightD(self, position):
        '''
        introduction:
        -
        input position(coordinate) and return its surrounding positions and values including eight directions.
        
        the order is ： ← ↖ ↘ ↑ ↓ ↙ ↗ →
        
        parameters: (`position`)
        -
        Note: input's position need to be equal to the format of (x, y).
        '''
        x = position[0]
        y = position[1]
        eightD_dict = {}
        for i, j in direction_iter(8):  # eightD_order : ← ↖ ↘ ↑ ↓ ↙ ↗ →
            try:
                if x + i < 0 or y + j < 0:
                    eightD_dict[(x+i, y+j)] = None
                else:
                    eightD_dict[(x+i, y+j)] = self.matrix[x+i][y+j]
            except:
                eightD_dict[(x+i, y+j)] = None
        return eightD_dict


    def up(self):
        '''
        Brief introduction:
        -
        update now's position to its upper position, and its value also change.
        '''
        now = [i for i in self.now][0]
        availables = self.fourD(now)
        now_up_position = list(availables.keys())[1]
        self.now = {now_up_position:availables[now_up_position]}


    def down(self):
        '''
        Brief introduction:
        -
        update now's position to its under position, and its value also change.
        '''
        now = [i for i in self.now][0]
        availables = self.fourD(now)
        now_down_position = list(availables.keys())[2]
        self.now = {now_down_position:availables[now_down_position]}


    def toleft(self):
        '''
        Brief introduction:
        -
        update now's position to its left position, and its value also change.
        '''
        now = [i for i in self.now][0]
        availables = self.fourD(now)
        now_left_position = list(availables.keys())[0]
        self.now = {now_left_position:availables[now_left_position]}


    def toright(self):
        '''
        Brief introduction:
        -
        update now's position to its right position, and its value also change.
        '''
        now = [i for i in self.now][0]
        availables = self.fourD(now)
        now_right_position = list(availables.keys())[-1]
        self.now = {now_right_position:availables[now_right_position]}


# ------------------------------------------------------------------------------
# #There are some samples:
# list1 = [[1,2,3,4],[5,6,7,8]]
# A = matrix(list1)
# x,y = 1,1
# value = 5
# position = (0,2) 
# A.matrix
# A.matrix[x][y]
# A.length
# A.columns
# A.width
# A.rows
# A.shape
# A.size
# A.matrix_dict
# A.get_position((x,y),return_first_one=False)
# A.get_value(position)
# A.now
# A.up()
# A.down()
# A.turnleft()
# A.turnright()
# A.fourD(position)
# A.eightD(position)
# ------------------------------------------------------------------------------
