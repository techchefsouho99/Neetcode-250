'''
* Longest Common Prefix : https://leetcode.com/problems/longest-common-prefix/description/
'''
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        numOfWords = len(strs)
        lComPre = ""
        firstStr = strs[0]
        for i in range(len(firstStr)):
            for j in range(1,numOfWords):
                if i == len(strs[j]) or firstStr[i] != strs[j][i]:
                    return lComPre
            lComPre+=firstStr[i]
        return lComPre


# ---- runnable test ----
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interview", "internet", "internal"],
        ["a"],
        []
    ]

    for strs in test_cases:
        print(f"Input: {strs}")
        print("Longest Common Prefix:", sol.longestCommonPrefix(strs))
        print("-" * 40)
