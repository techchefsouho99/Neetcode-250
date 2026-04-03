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
        # res = []
        # for ch in s:
        #     if ch == '(' or ch == '{' or ch == '[':
        #         res.append(ch)
        #     else:
        #         if ch == ')':
        #             if res and res[-1] == '(':
        #                 res.pop()
        #             else:
        #                 return False
        #         if ch == '}':
        #             if res and res[-1] == '{':
        #                 res.pop()
        #             else:
        #                 return False
        #         if ch == ']':
        #             if res and res[-1] == '[':
        #                 res.pop()
        #             else:
        #                 return False
        # return True if len(res) == 0 else False


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
