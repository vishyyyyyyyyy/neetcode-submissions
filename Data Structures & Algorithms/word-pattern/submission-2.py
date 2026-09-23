class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash = {}
        rvrs = {}
        words = s.split()
        if len(pattern) != len(words):
            return False

        i=0
        for char in pattern:
            if char not in hash:
                hash[char] = words[i]
            
            if words[i] not in rvrs:
                rvrs[words[i]] = char

            if char in hash and hash[char] != words[i]:
                return False
            if words[i] in rvrs and rvrs[words[i]] != char:
                return False



            i+=1
        return True