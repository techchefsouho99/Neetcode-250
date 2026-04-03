'''
* Two Sum : https://leetcode.com/problems/two-sum/description/
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seenMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seenMap:
                return [i , seenMap[diff]]
            seenMap[nums[i]] = i

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print("Indices of two numbers that add up to target:", result)
