'''
* Fibonacci Number : https://leetcode.com/problems/fibonacci-number/description
'''

class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        finVal = 0

        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
            finVal = c

        return a if n == 0 else (b if n == 1 else finVal)


if __name__ == "__main__":
    sol = Solution()

    n = int(input("Enter n: "))
    result = sol.fib(n)

    print(f"Fibonacci({n}) =", result)
