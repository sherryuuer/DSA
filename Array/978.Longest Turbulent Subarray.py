# https://leetcode.com/problems/longest-turbulent-subarray/description/
# arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
arr = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
# Output: 5
# Explanation: '' arr[0] >   arr[1] > arr[2] < arr[3] > arr[4] < arr[5] = arr[6]


class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def sign(a, b):
            if int(a) > int(b):
                return '<'
            elif int(a) < int(b):
                return '>'
            else:
                return '='
        maxlength = 1

        if len(arr) == 1:
            return 1

        presign = sign(arr[1], arr[0])
        curlength = 2 if presign != '=' else 1
        # print(presign)
        if len(arr) == 2:
            return curlength

        for i in range(2, len(arr)):
            cursign = sign(arr[i], arr[i - 1])

            if cursign != presign and cursign != '=':
                curlength += 1
            elif cursign == '=':
                curlength = 1
            else:
                curlength = 2
            presign = cursign

            maxlength = max(maxlength, curlength)
            # print(cursign, curlength, arr[i])
        return maxlength


solution = Solution()
res = solution.maxTurbulenceSize(arr)
print(res)


#####
class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l, r = 0, 1
        res, pre = 1, ''

        while r < len(arr):
            if arr[r - 1] < arr[r] and pre != '<':
                res = max(res, r - l + 1)
                r += 1
                pre = '<'
            elif arr[r - 1] > arr[r] and pre != '>':
                res = max(res, r - l + 1)
                r += 1
                pre = '>'
            else:
                r = r + 1 if arr[r - 1] == arr[r] else r
                l = r - 1
                pre = ''
        return res
