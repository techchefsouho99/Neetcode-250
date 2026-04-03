'''
* Longest Consecutive Sequence : https://leetcode.com/problems/longest-consecutive-sequence/description/
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet=set(nums)
        maxlen=0
        for num in numSet:
            counter = 1
            if (num - 1) not in numSet:
                while (num + counter) in numSet:
                     counter+=1
            maxlen = max(maxlen,counter)
        return maxlen
                    

# Example usage:
if __name__ == "__main__":  

    sol = Solution()
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4 (sequence: 1, 2, 3, 4)