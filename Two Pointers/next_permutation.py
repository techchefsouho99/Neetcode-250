'''
# Next Permutation - https://leetcode.com/problems/next-permutation
'''

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        r = n - 1
        idx = -1

        # Step 1: find the pivot
        while r > 0:
            if nums[r - 1] < nums[r]:
                idx = r - 1
                break
            r -= 1

        # Step 2: if no pivot, reverse whole array
        if idx == -1:
            nums.reverse()
            return

        # Step 3: find rightmost successor
        r = n - 1
        while nums[r] <= nums[idx]:
            r -= 1

        # Step 4: swap
        nums[r], nums[idx] = nums[idx], nums[r]

        # Step 5: reverse suffix
        nums[idx + 1:] = reversed(nums[idx + 1:])


def main():
    # Example usage
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    sol = Solution()
    sol.nextPermutation(nums)
    print("Next permutation:", nums)


if __name__ == "__main__":
    main()
