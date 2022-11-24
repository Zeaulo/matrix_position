
def is_matrix(matrix):
    '''
    Brief introduction:
    -
    Judge whether input can be converted into a matrix.
    '''
    if matrix == [] or matrix == () or matrix == None:
        raise NotImplementedError # Error : The matrix is empty.
    try:
        initial = len(matrix[0])
        for i in matrix[1:]:
            if len(i) != initial:
                raise TypeError # Error : Rows' length not coincident
    except:
        raise TypeError # Error : This does not conform to the matrix format.

def matrix_dict(matrix):
    '''
    Brief introduction:
    -
    Store all information in the matrix in a dictionary.

    format : `{(0, 1):value, (0,2):value, ... , (matrix length,matrix width):value}`
    '''
    dict1 = {}
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            try:
              dict1[(x, y)] = matrix[x][y]
            except:
              raise NotImplementedError  # Tip : We do not support the use of internal dictionaries yet
    return dict1

class direction_iter():
    def __init__(self, direction:int):
        if direction == 4:
            self.list = [0, -1, -1, 0, 1, 0, 0, 1] # fourD_orders : ← ↑ ↓ →
        elif direction == 8:
            self.list = [0, -1, -1, -1, 1, 1, -1, 0, 1, 0, 1, -1, -1, 1, 0, 1] # eightD_order : ← ↖ ↘ ↑ ↓ ↙ ↗ →
        self.index = 0
    def __next__(self):
        if self.index < len(self.list):
            temp = self.index
            self.index += 2
            return self.list[temp], self.list[temp + 1]
        else:
            raise StopIteration
    def __iter__(self):
        return self
