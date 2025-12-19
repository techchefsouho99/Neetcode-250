from typing import List

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n - 1
        leftMul, rightMul = 1, 1
        res = nums[0]
        for i in range(n):
            if leftMul == 0:
                leftMul = 1
            if rightMul == 0:
                rightMul = 1
            leftMul *= nums[i]
            rightMul *= nums[n - 1 - i]
            res = max(res, leftMul, rightMul)
        return res


# ---- Quick tests ----
if __name__ == "__main__":
    s = Solution()

    assert s.maxProduct([2, 3, -2, 4]) == 6
    assert s.maxProduct([-2, 0, -1]) == 0
    assert s.maxProduct([-2, 3, -4]) == 24
    assert s.maxProduct([0, 2]) == 2
    assert s.maxProduct([-2]) == -2
    assert s.maxProduct([1, -2, -3, 0, 7, -8, -2]) == 112

    print("All tests passed ✅")
