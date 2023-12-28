# https://leetcode.com/problems/reverse-bits/description/
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res
