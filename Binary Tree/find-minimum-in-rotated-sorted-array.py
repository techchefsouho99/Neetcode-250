from typing import List

class Solution(object):
    def findMin(self, nums: List[int]) -> int:
        """
        Find the minimum in a rotated sorted array (no duplicates).
        This keeps your original logic; only change is using // for integer division.
        """
        start, end = 0, len(nums) - 1
        mid = 0
        while start < end:
            if nums[start] < nums[end]:
                break
            mid = (end + start) // 2  # integer division for Python 3
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        return min(nums[start], nums[mid], nums[end])


# ---- Quick tests ----
if __name__ == "__main__":
    s = Solution()

    # Rotated arrays
    assert s.findMin([3,4,5,1,2]) == 1
    assert s.findMin([4,5,6,7,0,1,2]) == 0
    assert s.findMin([2,3,4,5,1]) == 1
    assert s.findMin([5,1,2,3,4]) == 1

    # Not rotated
    assert s.findMin([1,2,3,4,5]) == 1
    assert s.findMin([1]) == 1
    assert s.findMin([2,1]) == 1

    print("All tests passed ✅")
