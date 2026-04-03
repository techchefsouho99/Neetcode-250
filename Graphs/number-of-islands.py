'''
* Number Of Islands - https://leetcode.com/problems/number-of-islands/description
'''

from typing import List


class Solution:
    def dfs(self, i, j, m, n, grid, visited) -> None:
        if (
            i >= 0 and i < m and
            j >= 0 and j < n and
            grid[i][j] == "1" and
            visited[i][j] == -1
        ):
            visited[i][j] = 1
            self.dfs(i - 1, j, m, n, grid, visited)  # up
            self.dfs(i + 1, j, m, n, grid, visited)  # down
            self.dfs(i, j - 1, m, n, grid, visited)  # left
            self.dfs(i, j + 1, m, n, grid, visited)  # right

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)          # number of rows
        n = len(grid[0])       # number of columns
        visited = [[-1 for _ in range(n)] for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == -1:
                    count += 1
                    self.dfs(i, j, m, n, grid, visited)
                elif grid[i][j] == "0" and visited[i][j] == -1:
                    visited[i][j] = 1

        return count


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    sol = Solution()
    print("Number of Islands:", sol.numIslands(grid))
