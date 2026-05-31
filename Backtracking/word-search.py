'''
* Word Search: https://leetcode.com/problems/word-search/description
'''
from typing import List

class Solution:
    def iter(self, board: List[List[str]], r: int, c: int, word: str, idx: int) -> bool:
        # Entire word matched
        if idx == len(word):
            return True

        # Out of bounds or character mismatch
        if (
            r < 0
            or r >= len(board)
            or c < 0
            or c >= len(board[0])
            or board[r][c] != word[idx]
        ):
            return False

        # Mark current cell as visited
        temp = board[r][c]
        board[r][c] = '#'

        found = (
            self.iter(board, r - 1, c, word, idx + 1) or  # Up
            self.iter(board, r + 1, c, word, idx + 1) or  # Down
            self.iter(board, r, c - 1, word, idx + 1) or  # Left
            self.iter(board, r, c + 1, word, idx + 1)     # Right
        )

        # Backtrack
        board[r][c] = temp

        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.iter(board, r, c, word, 0):
                    return True
        return False


if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]

    solution = Solution()

    print(solution.exist(board, "ABCCED"))  # True
    print(solution.exist(board, "SEE"))     # True
    print(solution.exist(board, "ABCB"))    # False