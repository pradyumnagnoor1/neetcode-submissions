class Solution:
    def isValid(self, s: str) -> bool:

        my_stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in ['(','{','[']:
                my_stack.append(char)

            elif char in [')', ']', '}']:
                if not my_stack:
                    return False
                if my_stack[-1] == pairs[char]:
                    my_stack.pop()
                else:
                    return False

            else:
                return False

        return len(my_stack) == 0

        
        