'''
* Remove Element: https://leetcode.com/problems/remove-element
'''
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[right] == val:
                right -= 1
            else:
                if nums[left] == val:
                    nums[left] = nums[right]
                    right -= 1
                left += 1

        return left + 1


# -------- Test run --------
if __name__ == "__main__":
    sol = Solution()

    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = sol.removeElement(nums1, val1)
    print("Input:", [3, 2, 2, 3], "val =", val1)
    print("Output k =", k1)
    print("Modified array:", nums1[:k1])

    print()

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = sol.removeElement(nums2, val2)
    print("Input:", [0, 1, 2, 2, 3, 0, 4, 2], "val =", val2)
    print("Output k =", k2)
    print("Modified array:", nums2[:k2])
