class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        L = 0
        length = 0 #keeps track of length of window
        sett = set() #keep track of chars

        for R in range(len(s)):

            while s[R] in sett:
                sett.remove(s[L])
                L += 1

            sett.add(s[R])

            length = max(length, (R - L) + 1)


        return length
        