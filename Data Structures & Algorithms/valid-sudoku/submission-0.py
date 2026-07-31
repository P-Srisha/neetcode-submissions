class Solution:
    def isValid(self, board, startRow, endRow, startCol, endCol):
        cnt = [0] * 9
        for i in range(startRow, endRow):
            for j in range(startCol, endCol):
                if board[i][j].isdigit(): 
                    pos = int(board[i][j])
                    print(pos)
                    cnt[pos-1] += 1
        for num in cnt:
            if num > 1:
                return False   
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValid(board, i, i+1, 0, 9):
                return False
            if not self.isValid(board, 0, 9, i, i+1):
                return False
        for i in range(3):
            for j in range(3):
                if not self.isValid(board, 3*i, 3*(i+1), 3*j, 3*(j+1)):
                    return False

        return True