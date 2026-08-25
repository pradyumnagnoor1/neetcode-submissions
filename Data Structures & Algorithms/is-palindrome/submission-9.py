class Solution:
    def isPalindrome(self, s: str) -> bool:

        word = ''.join(char.lower() for char in s if char.isalnum())
        L = 0
        R = len(word) - 1


        while L < R:

            if word[L] != word[R]:
                return False

            L += 1
            R -= 1

        return True



        