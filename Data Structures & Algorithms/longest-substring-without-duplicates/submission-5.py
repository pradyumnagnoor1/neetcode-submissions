class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        longest = 0
        n = len(s)
        sett = set()


        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            width = (r - l) + 1
            sett.add(s[r])
            longest = max(longest, width)


        return longest

        