# Decode Ways - DP

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            # single-digit (1..9)
            if s[i - 1] in '123456789':
                dp[i] = dp[i - 1]
            # two-digit (10..26)
            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] in '0123456'):
                dp[i] += dp[i - 2]

        return dp[n]


# ---- Quick tests ----
if __name__ == "__main__":
    sol = Solution()
    assert sol.numDecodings("12") == 2        # "AB", "L"
    assert sol.numDecodings("226") == 3       # "BZ","VF","BBF"
    assert sol.numDecodings("06") == 0        # leading zero invalid
    assert sol.numDecodings("0") == 0
    assert sol.numDecodings("10") == 1        # "J"
    assert sol.numDecodings("") == 0
    assert sol.numDecodings("11106") == 2     # "AAJF","KJF" invalid splits filtered
    assert sol.numDecodings("2101") == 1      # "UJA"
    print("All tests passed ✅")
