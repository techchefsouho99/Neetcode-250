from typing import List

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0


# ---- Quick tests ----
if __name__ == "__main__":
    def run_case(mat, expected):
        s = Solution()
        s.setZeroes(mat)
        assert mat == expected, f"\nGot:      {mat}\nExpected: {expected}"

    run_case(
        [[1,1,1],[1,0,1],[1,1,1]],
        [[1,0,1],[0,0,0],[1,0,1]]
    )

    run_case(
        [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
        [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    )

    run_case(
        [[1,2,3,4]],
        [[1,2,3,4]]
    )

    run_case(
        [[1,0,3,4]],
        [[0,0,0,0]]
    )

    run_case(
        [[1],[0],[3]],
        [[0],[0],[0]]
    )

    run_case(
        [[0]],
        [[0]]
    )

    print("All tests passed ✅")
