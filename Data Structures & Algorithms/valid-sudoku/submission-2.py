class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if board[r][c].isdigit():
                    num = int(board[r][c])
                    if (rows[r] >> num) & 1 or (cols[c] >> num) & 1 or (squares[r // 3 * 3 + c // 3] >> num) & 1:
                        return False                
                    rows[r] |= (1 << num) 
                    cols[c] |= (1 << num)
                    squares[r // 3 * 3 + c // 3] |= (1 << num)  
        return True