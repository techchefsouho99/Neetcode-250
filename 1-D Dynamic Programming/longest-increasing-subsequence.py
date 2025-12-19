from typing import List

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


# ---- Quick tests ----
if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert s.lengthOfLIS([0,1,0,3,2,3]) == 4
    assert s.lengthOfLIS([7,7,7,7,7]) == 1
    assert s.lengthOfLIS([1]) == 1
    assert s.lengthOfLIS([4,10,4,3,8,9]) == 3
    print("All tests passed ✅")
