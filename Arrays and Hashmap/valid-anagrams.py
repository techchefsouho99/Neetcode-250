'''
* 242. Valid Anagrams: https://leetcode.com/problems/valid-anagram/description/
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            sMap , tMap = {} , {}
            for i in range(len(s)):
                sMap[s[i]] = 1 + sMap.get(s[i],0)
                tMap[t[i]] = 1 + tMap.get(t[i],0)
            return sMap == tMap

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    s1 = "listen"
    t1 = "silent"
    print("Input:", s1, t1)
    print("Output:", solution.isAnagram(s1, t1))  # True

    # Test Case 2
    s2 = "rat"
    t2 = "car"
    print("\nInput:", s2, t2)
    print("Output:", solution.isAnagram(s2, t2))  # False

    # Test Case 3
    s3 = "aacc"
    t3 = "ccac"
    print("\nInput:", s3, t3)
    print("Output:", solution.isAnagram(s3, t3))  # False
