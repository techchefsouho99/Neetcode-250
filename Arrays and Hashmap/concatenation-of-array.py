'''
* Concatenation Of Array: https://leetcode.com/problems/concatenation-of-array/description/
'''

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums.append(nums[i])
        return nums


if __name__ == "__main__":
    nums = [1, 2, 3]

    sol = Solution()
    result = sol.getConcatenation(nums)

    print("Concatenated array:", result)
