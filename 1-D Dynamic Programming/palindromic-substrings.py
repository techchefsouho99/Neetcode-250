# Palindromic Substrings - expand around center

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        for i in range(n):

            # odd-length palindromes centered at i
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            # even-length palindromes centered between i and i+1
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count


# ---- Quick tests ----
if __name__ == "__main__":
    s = Solution()
    assert s.countSubstrings("abc") == 3      # a, b, c
    assert s.countSubstrings("aaa") == 6      # a,a,a, aa,aa, aaa
    assert s.countSubstrings("") == 0
    assert s.countSubstrings("abba") == 6     # a,b,b,a, bb, abba
    assert s.countSubstrings("racecar") == 10 # singles(7) + "cec","aceca","racecar"
    print("All tests passed ✅")
