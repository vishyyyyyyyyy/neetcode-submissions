class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rvrs = s[::-1]
        count = 0
        for a in rvrs:

            if a== " " and count ==0:
                continue
            if a == " ":
                return count
            
            count+=1
        
        return count