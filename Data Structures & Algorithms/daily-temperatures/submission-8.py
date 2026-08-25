class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        my_stack = []

        result = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            while my_stack and n > my_stack[-1][0]:
                stackT, stackI = my_stack.pop()
                result[stackI] = i - stackI

            my_stack.append((n,i))

        return result

        



        