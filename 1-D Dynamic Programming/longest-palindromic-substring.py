# Longest Palindromic Substring - expand around center

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        strIdx = 0
        maxLen = 0
        for i in range(n):

            # odd-length center at i
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    strIdx = l
                    maxLen = r - l + 1
                l -= 1
                r += 1

            # even-length center between i and i+1
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    strIdx = l
                    maxLen = r - l + 1
                l -= 1
                r += 1

        return s[strIdx: strIdx + maxLen]


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
