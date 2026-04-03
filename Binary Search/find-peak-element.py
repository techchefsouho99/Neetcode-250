'''
* Find Peak ELement: https://leetcode.com/problems/find-peak-element/description
'''
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            # check right neighbor
            if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                start = mid + 1

            # check left neighbor
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                end = mid - 1

            else:
                return mid


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 5, 6, 4]

    sol = Solution()
    peak_index = sol.findPeakElement(nums)

    print("Array:", nums)
    print("Peak index:", peak_index)
    print("Peak value:", nums[peak_index])
