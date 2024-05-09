# https://leetcode.com/problems/single-number-iii/description/

def two_single_numbers(nums):
    xor = 0
    for num in nums:
        xor ^= num

    print(xor)

    mask = xor & -xor
    print(bin(mask))

    first = 0

    for num in nums:
        if num & mask:
            first ^= num
    return [first, xor ^ first]


nums = [1, 2, 3, 1, 2, 4]
print(two_single_numbers(nums))


def two_single_numbers(nums):
    num_dict = set()
    for n in nums:
        if n not in num_dict:
            num_dict.add(n)
        else:
            num_dict.remove(n)
    return list(num_dict)


print(bool(1))
