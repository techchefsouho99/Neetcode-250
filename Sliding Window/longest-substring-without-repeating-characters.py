# Longest Substring Without Repeating Characters - given implementation

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        NOTE: This implementation resets the window on any repeat.
        """
        counter = 0
        finmax = 0
        temp_map = {}
        for ch in s:
            if ch in temp_map:
                temp_map = {}
                counter = 0
            temp_map[ch] = 1
            counter = counter + 1
            finmax = max(finmax, counter)
        return finmax


# ---- Simple demo run ----
if __name__ == "__main__":
    sol = Solution()
    examples = [
        "",             # -> 0
        "abcabcbb",     # -> (this impl returns 3)
        "bbbbb",        # -> 1
        "pwwkew",       # -> 3
    ]
    for s in examples:
        print(f"lengthOfLongestSubstring({s!r}) = {sol.lengthOfLongestSubstring(s)}")
