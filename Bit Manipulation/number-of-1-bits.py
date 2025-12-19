# Hamming Weight / Number of 1 Bits

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        Counts set bits using Brian Kernighan's algorithm.
        Time: O(k) where k = number of set bits; Space: O(1)
        """
        count = 0
        while n:
            n &= (n - 1)  # clear the lowest set bit
            count += 1
        return count


# ---- Quick tests ----
if __name__ == "__main__":
    s = Solution()
    assert s.hammingWeight(11) == 3          # 1011 -> 3
    assert s.hammingWeight(128) == 1         # 10000000 -> 1
    assert s.hammingWeight(2147483645) == 30 # many 1s
    print("All tests passed ✅")
