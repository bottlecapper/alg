
"""
Sudoku, Backtracking
"""

class Solution:
    def isValidSudoku(self, board):
        Row = [[] for i in range(9)]
        Col = [[] for i in range(9)]
        Box = [[] for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                k = (i//3)*3 + j//3
                if board[i][j] in Row[i]+Col[j]+Box[k]:
                    return False
                Row[i].append(board[i][j])
                Col[j].append(board[i][j])
                Box[k].append(board[i][j])

        return True


    def possibleValue(self, board, i, j):
        Row = board[i]
        Col = [board[x][j] for x in range(9)]
        m, n = (i//3)*3, (j//3)*3
        Box = [board[m+dm][n+dn] for dm in range(3) for dn in range(3)]
        possible = []
        for num in range(1,10):
            if str(num) not in Row+Col+Box:
                possible.append(str(num))
        return possible


    def sudokuSolve(self, board):
        if '.' not in sum(board, []):
            print('Sudoku successfully solved!')
            print(board)
            return

        i, j = 0, 0
        for x in range(9):
            for y in range(9):
                if board[x][y] == '.':
                    i, j = x, y
                    break
            else:
                continue
            break

        possible = self.possibleValue(board, i, j)
        for item in possible:
            board[i][j] = item
            self.sudokuSolve(board)
        # Backtracking
        board[i][j] = '.'



def main():
    Sudoku = Solution()
    # board = [[".",".","9","7","4","8",".",".","."],
    #          ["7",".",".",".",".",".",".",".","."],
    #          [".","2",".","1",".","9",".",".","."],
    #          [".",".","7",".",".",".","2","4","."],
    #          [".","6","4",".","1",".","5","9","."],
    #          [".","9","8",".",".",".","3",".","."],
    #          [".",".",".","8",".","3",".","2","."],
    #          [".",".",".",".",".",".",".",".","6"],
    #          [".",".",".","2","7","5","9",".","."]]

    board = [[".",".",".",".",".","4",".",".","."],
             ["5",".","7","3","2",".","8",".","."],
             [".",".",".","1","5","6",".",".","."],
             ["9",".",".",".","1",".",".",".","6"],
             ["2","8",".","9","4","7",".","1","3"],
             ["1",".",".",".","8",".",".",".","4"],
             [".",".",".","4","3","5",".",".","."],
             [".",".","2",".","6","8","4",".","9"],
             [".",".",".","2",".",".",".",".","."]]

    print(Sudoku.isValidSudoku(board))
    Sudoku.sudokuSolve(board)

if __name__ == "__main__":
    main()
