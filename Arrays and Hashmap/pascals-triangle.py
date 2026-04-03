'''
* Pascal's Triangle : https://leetcode.com/problems/pascals-triangle/description/
'''
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        # using arrays
        # for i in range(numRows):
        #     if i == 0:
        #         res.append([1])
        #     elif i == 1:
        #         res.append([1,1])
        #     else:
        #         temp = []
        #         temp.append(1)
        #         for j in range(1,i):
        #             temp.append(res[i-1][j-1]+res[i-1][j])
        #         temp.append(1)
        #         res.append(temp)
        # return res

        # using dynamic programming
        for i in range(numRows):
            dp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    dp.append(1)
                else:
                    dp.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(dp)
        return res


# ---- test run ----
if __name__ == "__main__":
    sol = Solution()
    numRows = 5
    print(sol.generate(numRows))
