class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        for num in g: 
            for i in range(len(s)):
                if s[i] >= num:
                    count +=1
                    del s[i]
                    break

        return count