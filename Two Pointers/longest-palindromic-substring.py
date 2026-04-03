# Longest Palindromic Substring - expand around center

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        resStr = ""
        resLen = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                strLen = r - l + 1
                if resLen < strLen:
                    resLen = strLen
                    resStr = s[l:r+1]
                l-=1
                r+=1
            l , r = i , i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                strLen = r - l + 1
                if resLen < strLen:
                    resLen = strLen
                    resStr = s[l:r+1]
                l-=1
                r+=1
        return resStr


# ---- Quick tests ----
if __name__ == "__main__":
    s = Solution()
    assert s.longestPalindrome("babad") in ("bab", "aba")
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("a") == "a"
    assert s.longestPalindrome("ac") in ("a", "c")
    assert s.longestPalindrome("") == ""
    assert s.longestPalindrome("aaaa") == "aaaa"
    assert s.longestPalindrome("racecar") == "racecar"
    print("All tests passed ✅")
