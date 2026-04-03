'''
* Move Zeroes : https://leetcode.com/problems/move-zeroes/description
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, r = 0, 0

        for r in range(l, n):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]

    sol = Solution()
    sol.moveZeroes(nums)

    print("After moving zeroes:", nums)
