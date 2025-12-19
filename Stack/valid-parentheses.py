# Valid Parentheses - Full working script with tests

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


# ---- Run tests when executed directly ----
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("[{()}]", True),
        ("[{(})]", False),
    ]
    for s, expected in tests:
        got = sol.isValid(s)
        assert got == expected, f"Input: {s} | Expected: {expected}, Got: {got}"
    print("All tests passed ✅")
