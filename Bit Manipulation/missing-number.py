from typing import List

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res


# ---- Quick tests ----
if __name__ == "__main__":
    s = Solution()
    assert s.missingNumber([3, 0, 1]) == 2
    assert s.missingNumber([0, 1]) == 2
    assert s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert s.missingNumber([0]) == 1
    assert s.missingNumber([]) == 0  # edge case: n=0
    print("All tests passed ✅")
