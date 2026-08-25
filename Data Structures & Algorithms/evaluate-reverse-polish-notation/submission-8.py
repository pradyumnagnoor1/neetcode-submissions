class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for char in tokens:
            if char == '+':
                res = stack.pop() + stack.pop()
                stack.append(res)

            elif char == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a-b)

            elif char == '*':
                res = stack.pop() * stack.pop()
                stack.append(res)

            elif char == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a/b))

            else:
                stack.append(int(char))

        return stack[0]

        