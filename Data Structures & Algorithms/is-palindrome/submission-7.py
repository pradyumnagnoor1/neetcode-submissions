class Solution:
    def isPalindrome(self, s: str) -> bool:

        noSpace_string = ""

        for char in s:
            if char.isalnum():
                noSpace_string += char.lower()

        return noSpace_string == noSpace_string[::-1]




        