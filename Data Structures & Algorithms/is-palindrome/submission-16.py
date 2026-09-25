class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.replace(" ", "").lower()
        new_word = ""

        for char in word:
            if char.isalnum():
                new_word += char


        L = 0
        R = len(new_word) - 1

        while L < R:
            if new_word[L] != new_word[R]:
                return False

            else:
                R -= 1
                L += 1

        return True
        