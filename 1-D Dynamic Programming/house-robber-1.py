from typing import List

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


# ---- Quick tests ----
if __name__ == "__main__":
    s = Solution()

    assert s.rob([]) == 0
    assert s.rob([1]) == 1
    assert s.rob([2, 7, 9, 3, 1]) == 12
    assert s.rob([2, 1, 1, 2]) == 4
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 1]) == 2
    assert s.rob([2, 7, 3]) == 9

    print("All tests passed ✅")
