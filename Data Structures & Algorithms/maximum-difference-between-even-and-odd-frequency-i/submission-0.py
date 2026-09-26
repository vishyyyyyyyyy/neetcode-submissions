class Solution:
    def maxDifference(self, s: str) -> int:
        hash = {}

        for char in s:
            hash[char] = hash.get(char, 0) + 1

        a1 = 0
        a2 = len(s)

        for char in hash:
            if hash[char] % 2 ==1 and hash[char] >= a1:
                a1 = hash[char] 
            if hash[char]  % 2 ==0 and hash[char]  <=a2:
                a2 = hash[char] 
        return(a1-a2)

        