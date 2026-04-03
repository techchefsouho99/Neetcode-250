'''
* Decrypt String From Alphabet To Integer Mapping - 
*    https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description
'''

class Solution:
    def freqAlphabets(self, s: str) -> str:
        finStr = ""
        i = len(s) - 1

        while i >= 0:
            if s[i] == '#':
                temp = s[i-2] + s[i-1]
                finStr += chr(int(temp) + 96)
                i -= 3
            else:
                finStr += chr(int(s[i]) + 96)
                i -= 1

        return finStr[::-1]


def main():
    s = input("Enter encoded string: ").strip()
    sol = Solution()
    result = sol.freqAlphabets(s)
    print("Decoded string:", result)


if __name__ == "__main__":
    main()
