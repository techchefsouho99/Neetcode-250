'''
* Romove Element: https://leetcode.com/problems/remove-element/description/
'''

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l


# ---- runnable test ----
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([3, 2, 2, 3], 3),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2),
        ([], 1),
        ([1, 1, 1], 1),
        ([4, 5], 3)
    ]

    for nums, val in test_cases:
        k = sol.removeElement(nums, val)
        print(f"Input nums: {nums}, val: {val}")
        print(f"New length: {k}")
        print(f"Modified array (first k elements): {nums[:k]}")
        print("-" * 50)
