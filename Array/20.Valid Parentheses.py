# https://leetcode.com/problems/valid-parentheses/

# Example 2:

# s = "()[]{}"
# Output: true
# Example 3:

s = "(]"
# Output: false

# must be in the correct order!! ([)] this is wrong.


class mySolution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '[', '{']
        right = [')', ']', '}']
        stacks = []
        for c in s:
            if c in left:
                stacks.append(c)
            elif c in right:
                if len(stacks) == 0:
                    return False
                pair_idx = right.index(c)
                last = stacks.pop()
                if last == left[pair_idx]:
                    continue
                else:
                    return False

        if len(stacks) != 0:
            return False
        return True

    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stacks = []
        charmap = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in charmap:
                if stacks:
                    if charmap[c] == stacks.pop():
                        continue
                    else:
                        return False
            else:
                stacks.append(c)

        return not stacks


so = mySolution()
print(so.isValid2(s))
