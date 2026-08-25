class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0
        L = 0
        my_set = set()

        for R in range(len(s)):

            while s[R] in my_set:
                my_set.remove(s[L])
                L += 1
                

            my_set.add(s[R])

            length = max(length, R - L + 1)

        return length

        
        