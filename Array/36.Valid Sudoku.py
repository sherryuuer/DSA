# 判断一个99数独盘是否有效，这里的有效有如下规则
# 行1-9不重复，列1-9不重复，小box1-9不重复，无需在意是否可以解决
board1 = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]
# Output: true


board2 =[
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]
# Output: false


class Solution:
    def isValidSudoku(self, board):
        from collections import defaultdict
        rows = defaultdict(set) # key r
        cols = defaultdict(set) # key c
        boxs = defaultdict(set) # key (r // 3, c // 3)

        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            for c in range(COLS):

                num = board[r][c]

                if num == ".":
                    continue

                if (num in rows[r] or num in cols[c] or num in boxs[(r // 3, c // 3)]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxs[(r // 3, c // 3)].add(num)

        return True


solution = Solution()
res1 = solution.isValidSudoku(board1)
res2 = solution.isValidSudoku(board2)
print(res1, res2)