# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# input: n = 3
# output:
# ['()(())', '((()))', '()()()', '(())()', '(()())']
# ()
# input: n = 1, output: ['()']

# '' top <= '(': 3, ')': 3
# solution1:
# steps
# edge case: n == 1: return ['()']
# prepare: result = [], subset = [], length = 0
# 1, while n > 0, n--
# 2, insert the () into the '', righthand must be after the lefthand: insert(length, '('), length++, insert(length, )
# 3, after every insert, append the subset answer, ''.join(subset)
# 4, return the result


def generateParenthesis(n):
    def backtrack(current, open_count, close_count):
        # Base case: If the current string has 2*n characters, it's a valid combination
        if len(current) == 2 * n:
            result.append(current)
            return

        # If we can still add an opening parenthesis, do so
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        # If we can add a closing parenthesis without violating the balance, do so
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    result = []
    backtrack('', 0, 0)
    return result


# Test
n = 3
print(generateParenthesis(n))


def generateParenthesis2(n):
    stack = []
    res = []

    def backtrack(open_count, close_count):
        if open_count == close_count == n:
            res.append(''.join(stack))

        if open_count < n:
            stack.append('(')
            backtrack(open_count + 1, close_count)
            stack.pop()

        if close_count < open_count:
            stack.append(')')
            backtrack(open_count, close_count + 1)
            stack.pop()

    backtrack(0, 0)
    return res


# Test
n = 3
print(generateParenthesis2(n))
