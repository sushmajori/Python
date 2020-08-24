

# class QueenChessBoard.
class QueenChessBoard:
    def __init__(self, size):
        self.size = size # board has dimensions size x size
                        #  after all queens are placed, they will be at positions colum[0][0],[1][1]
        self.columns = [] # list for stored board c
 
    def place_in_next_row(self, column): # methods to place a queen in the next row given in the column.
        self.columns.append(column)
 
    def remove_in_current_row(self): # remove the queen from the last row if a queen is present
        return self.columns.pop()
 
    def is_this_column_safe_in_next_row(self, column): #check whether a given column is safe to place a queen in the next free row.
        # index of next row
        row = len(self.columns)
 
        # check column
        for queen_column in self.columns:
            if column == queen_column:
                return False
 
        # check diagonal
        for queen_row, queen_column in enumerate(self.columns):
            if queen_column - queen_row == column - row:
                return False
 
        # check other diagonal
        for queen_row, queen_column in enumerate(self.columns):
            if ((self.size - queen_column) - queen_row
                == (self.size - column) - row):
                return False
 
        return True
 
    def display(self):
        for row in range(self.size):
            for column in range(self.size):
                if column == self.columns[row]:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()
 
 
def solve_queen(size): # this function takes the size of the board as argument.
    board = QueenChessBoard(size)
    number_of_solutions = 0
    row = 0
    column = 0
    # iterate over rows of board
    while True:
        # place queen in next row
        #it is checked which column a queen can be placed in the first available row of the board.
        while column < size:
            if board.is_this_column_safe_in_next_row(column):
                board.place_in_next_row(column)
                row += 1
                column = 0
                break
            else:
                column += 1
 
        # if could not find column to place in or if board is full
        if (column == size or row == size):
            # if board is full,  then we have a solution
            if row == size:
                board.display()
                print()
                number_of_solutions += 1
                board.remove_in_current_row()
                row -= 1
 
            # now backtrack
            #Backtracking is done by removing the queen from the last filled row and making the next iteration 
            try:
                prev_column = board.remove_in_current_row()
            except IndexError:
                # all queens removed
                # thus no more possible configurations
                break
            # try previous row again
            row -= 1
            # start checking at column = (1 + value of column in previous row)
            column = 1 + prev_column
 
    print('Number of solutions:', number_of_solutions)
 
 
n = int(input('Enter n: '))
solve_queen(n)






