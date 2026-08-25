class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        my_stack = []

        for char in tokens:
            if char == '+':
                my_stack.append(my_stack.pop() + my_stack.pop())

            elif char == '*':
                my_stack.append(my_stack.pop() * my_stack.pop())

            elif char == '-':
                a = my_stack.pop()
                b = my_stack.pop()

                my_stack.append(b-a)

            elif char == '/':
                a = my_stack.pop()
                b = my_stack.pop()
                my_stack.append(int(float(b) / a))

            else:
                my_stack.append(int(char))

        return my_stack[0]


        