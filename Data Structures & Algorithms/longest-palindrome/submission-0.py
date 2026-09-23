class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1

        hash = {}

        for char in s:
            hash[char] = hash.get(char, 0) +1
        
        odd= False
        length = 0
        for key in hash:
            if hash[key]% 2 == 0:
                length += hash[key]
            else:
                length+=hash[key]-1
                odd=  True
        if odd == True:
            return length +1
        return length