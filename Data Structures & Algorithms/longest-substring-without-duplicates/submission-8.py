class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        sett = set()


        for R in range(len(s)):

            while s[R] in sett: #if a duplicate is encountered
                sett.remove(s[L]) #remove the character at s[L] from set
                L += 1 # move left pointer once to maintain valid window


            sett.add(s[R]) #if character not already in set then just add it

            length = max(length, (R - L) + 1) #find max length of sliding window

        return length