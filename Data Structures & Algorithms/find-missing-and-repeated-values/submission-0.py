class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        count = 0
        seen = set()

        for arr in grid:
            for num in arr:
                if num in seen:
                    ans.append(num)
                seen.add(num)
                count +=1

        for num in range(1, count + 1):
            if num not in seen:
                ans.append(num)
        return ans