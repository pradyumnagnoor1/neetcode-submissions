class Solution:
    def calPoints(self, operations: List[str]) -> int:

        my_stack = []
        

        for operation in operations:
            if operation == '+':
                my_stack.append(my_stack[-1] + my_stack[-2])

            elif operation == 'D':
                my_stack.append(2 * my_stack[-1])

            elif operation == 'C':
                my_stack.pop()

            else:
                my_stack.append(int(operation))

        return sum(my_stack)


            
        