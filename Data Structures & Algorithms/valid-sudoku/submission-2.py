class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowseen = set()

        for row in board:
            for num in row:
                if num != ".":
                    if num not in rowseen:
                        rowseen.add(num)
                    else:
                        return False
            rowseen.clear()
        
        for col in range(9):
            colseen= set()

            for row in range(9):
                num = board[row][col]
                if num != ".":
                    if num in colseen:
                        return False
                    colseen.add(num)
        for boxrow in range(0, 9, 3):
            for boxcol in range(0, 9, 3):
                seen = set()

                for row in range(boxrow, boxrow + 3):
                    for col in range(boxcol, boxcol + 3):
                        num = board[row][col]

                        if num != ".":
                            if num in seen:
                                return False
                            seen.add(num)
        
        return True