class Solution:
    def findLucky(self, arr: List[int]) -> int:
        seen ={}

        for num in arr:
            seen[num] = seen.get(num, 0) + 1
        
        arr = []


        for key, value in seen.items():
            if key == value:
               arr.append(key)
            else: 
                continue

        if len(arr) > 0:
            return max(arr)
        
        return -1