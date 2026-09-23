class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        sort = sorted(heights)

        for i in range(len(heights)):
            if sort[i]!= heights[i]:
                count+=1
        
        return count