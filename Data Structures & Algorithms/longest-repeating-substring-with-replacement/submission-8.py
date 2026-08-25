class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        length = 0 #length of window 
        maxFreq = 0 # tracks the number of times a specific value exists
        L = 0 
        count = {} #dict to store number of times each char exists


        for R in range(len(s)):

            count[s[R]] = count.get(s[R], 0) + 1 #updates count of curr char

            maxFreq = max(maxFreq, count[s[R]])

            if (R - L + 1) - maxFreq > k: #if the size of window minus maxfreq of char is greater than k
                count[s[L]] -= 1 #the count of the character at s[L] decreases by 1
                L += 1 #moves left pointer forward

            length = max(length, R - L + 1)

        return length

        