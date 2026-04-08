class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if board[r][c].isdigit():
                    num = int(board[r][c])
                    if num in rows[r] or num in cols[c] or num in squares[r // 3 * 3 + c // 3]:
                        return False
                    rows[r].add(num)
                    cols[c].add(num)
                    squares[r // 3 * 3 + c // 3].add(num)
        return True