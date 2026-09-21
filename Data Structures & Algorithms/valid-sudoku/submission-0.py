class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m=len(board)
        n=len(board[0])
        rows=[set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        bxs = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                num = board[r][c]
                bx = (r//3)*3 +(c//3)

                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                if num in bxs[bx]:
                    return False
                rows[r].add(num)

                cols[c].add(num)
                bxs[bx].add(num)
        return True

