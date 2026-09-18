class Solution:
    def isPalindrome(self, s: str) -> bool:
        seen = []

        for word in s:
            if word.isalnum():
                seen.append(word.lower())
        
        rvrsd = seen[::-1]

        return( seen == rvrsd)