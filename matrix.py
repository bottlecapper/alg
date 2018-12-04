
"""
Matrix Operations
"""

class Solution:
    def matrixTranspose(self, matrix):
        if matrix == []:
            return []
        nrow = len(matrix)
        ncol = len(matrix[0])
        matrix_T = [[matrix[i][j] for i in range(nrow)] for j in range(ncol)]
        return matrix_T

    def matrixRotate(self, matrix):
        if matrix == []:
            return []
        nrow = len(matrix)
        ncol = len(matrix[0])
        matrix_R = [[matrix[i][j] for i in range(nrow - 1, -1, -1)] for j in range(ncol)]
        return matrix_R

    def matrixFlipRows(self, matrix):
        if matrix == []:
            return []
        nrow = len(matrix)
        ncol = len(matrix[0])
        matrix_FR = [[matrix[j][i] for i in range(nrow)] for j in range(ncol-1,-1,-1)]
        return matrix_FR

    def matrixFlipCols(self, matrix):
        if matrix == []:
            return []
        nrow = len(matrix)
        ncol = len(matrix[0])
        matrix_FC = [[matrix[j][i] for i in range(nrow-1,-1,-1)] for j in range(ncol)]
        return matrix_FC


def main():
    op = Solution()
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]

    print(matrix)
    matrix_T = op.matrixTranspose(matrix)
    matrix_R = op.matrixRotate(matrix)
    matrix_FR = op.matrixFlipRows(matrix)
    matrix_FC= op.matrixFlipCols(matrix)
    print('Transpose:', matrix_T)
    print('Rotate:', matrix_R)
    print('FlipRow:', matrix_FR)
    print('FlipCol:', matrix_FC)


if __name__ == "__main__":
    main()
