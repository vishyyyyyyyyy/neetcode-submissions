class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0
        for s in details:
            b=""
            b= s[11]+ s[12]
            if int(b) > 60:
                count +=1
            
        
        return count
        
