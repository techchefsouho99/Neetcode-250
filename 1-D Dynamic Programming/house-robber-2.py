from typing import List

class Solution(object):
    def rob(self, nums):
        """
        House Robber II (circular). Uses two linear runs:
        - Exclude first house: nums[1:]
        - Exclude last house:  nums[:-1]
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(nums[0], self.houseRob(nums[1:]), self.houseRob(nums[:-1]))

    def houseRob(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            newRob = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2


# ---- Quick tests ----
if __name__ == "__main__":
    s = Solution()
    assert s.rob([2, 3, 2]) == 3
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([1, 2, 3]) == 3
    assert s.rob([1]) == 1
    assert s.rob([0]) == 0
    assert s.rob([200, 3, 140, 20, 10]) == 340
    print("All tests passed ✅")
