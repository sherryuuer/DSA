# https://leetcode.com/problems/complement-of-base-10-integer/description/

from math import log2, floor


class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        x = 1
        while x <= n:
            x <<= 1
        return (x - 1) ^ n


# or
def find_bitwise_complement(num):
    if num == 0:
        return 1

    bit_count = floor(log2(num)) + 1
    all_bits_set = (1 << bit_count) - 1
    return num ^ all_bits_set


x = 1
while x <= 5:
    x <<= 1
    # print(bin(x))

bit_count = floor(log2(8))
print(bin(bit_count))
print(bin(8))
print(bit_count)
# all_bits_set = (1 << bit_count) - 1
# print(all_bits_set)
# print(5 ^ 7)
# print(bin(7))
