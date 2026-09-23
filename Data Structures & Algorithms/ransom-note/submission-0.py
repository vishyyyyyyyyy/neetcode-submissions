class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #hash both
        #compare ransom to magazine and subtract instances occured

        r= {}
        m={}
        for char in ransomNote:
            r[char] = r.get(char, 0)+1
        for char in magazine:
            m[char] = m.get(char, 0) +1

        for key in r:
            for i in range(r[key]):
                if key not in m or m[key] == 0:
                    return False
                m[key] -=1
            
        return True

