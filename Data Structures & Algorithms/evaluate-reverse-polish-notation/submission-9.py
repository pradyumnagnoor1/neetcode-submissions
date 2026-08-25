class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []

        for token in tokens:
            if token == '+':
                second = my_stack.pop()
                first = my_stack.pop()

                my_stack.append(first+second)

            elif token == '-':
                second = my_stack.pop()
                first = my_stack.pop()
                my_stack.append(first - second)

            elif token == '*':
                second = my_stack.pop()
                first = my_stack.pop()
                my_stack.append(first * second)

            elif token == '/':
                second = my_stack.pop()
                first = my_stack.pop()
                my_stack.append(int(first/second))

            else:
                my_stack.append(int(token))


        return my_stack[-1]

            



        