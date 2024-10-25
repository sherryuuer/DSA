class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        opes = {"+", "-", "*", "/"}
        stack = []

        for t in tokens:
            if t not in opes:
                stack.append(int(t))
                continue

            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            elif t == "/":
                stack.append(a // b if a // b > 0 else 0)

        return stack.pop()


tokens1 = ["2", "1", "+", "3", "*"]
# Output: 9

tokens2 = ["4", "13", "5", "/", "+"]
# Output: 6

tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22

solution = Solution()
print(solution.evalRPN(tokens1))
print(solution.evalRPN(tokens2))
print(solution.evalRPN(tokens3))
