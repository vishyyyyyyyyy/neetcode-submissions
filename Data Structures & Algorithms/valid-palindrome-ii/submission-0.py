class Solution:
    def validPalindrome(self, s: str) -> bool:
        seen = []

        for i in range(len(s)):
            temp = s[:i]+s[i+1:]
            if temp[::-1] == temp:
                return True

        for l in s:
            seen.append(l)

        if seen[::-1] != seen:
            return False

        return True
        