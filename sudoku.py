class Solver():
    def __init__(self, bo:list):
        self.board_orig = [tuple(row) for row in bo]
        self.board = bo
        if self.check_board():
            self.solve()

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def validate(self, num, pos):
        # validate row
        for k in range(len(self.board[pos[0]])):
            if num == self.board[pos[0]][k] and k!=pos[1]:
                return False

        # validate column
        for row in range(len(self.board)):
            if num == self.board[row][pos[1]] and row != pos[0]:
                return False

        # check cell
        cell_x = pos[1] // 3
        cell_y = pos[0] // 3

        for i in range(3*cell_y, 3*cell_y + 3):
            for j in range(3*cell_x, 3*cell_x + 3):
                if num == self.board[i][j] and (i, j) != pos:
                    return False
        
        return True

    def check_board(self):
        filled = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] != 0:
                    filled.append((i,j))

        valid = True
        for pos in filled:
            valid = valid and self.validate(self.board[pos[0]][pos[1]], pos)
        
        return valid

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True

        for i in range(1,10):
            if self.validate(i, empty):
                self.board[empty[0]][empty[1]] = i

                if self.solve():
                    return True
                
                self.board[empty[0]][empty[1]] = 0
        
        return False

# bo = [[0, 5, 0, 1, 0, 0, 0, 0, 0], [2, 0, 4, 0, 0, 0, 0, 9, 3], [0, 0, 0, 0, 0, 3, 4, 5, 0], [7, 2, 1, 0, 3, 8, 6, 4, 0], [4, 3, 0, 0, 5, 7, 9, 8, 1], [0, 0, 0, 0, 6, 1, 0, 0, 2], [0, 0, 0, 0, 0, 4, 0, 0, 9], [1, 0, 5, 3, 0, 0, 8, 0, 0], [6, 4, 0, 8, 0, 2, 0, 0, 0]]
# bo = [[1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# print(bo)
# s = Solver(bo)
# print(s.check_board())
# print(s.board)    
# print(s.board_orig)