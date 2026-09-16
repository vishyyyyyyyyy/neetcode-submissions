class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # create a hashset
    # iterate through the list once and add all the nums and update the     count to the hashset
    #check which keys  == k
    #return(list(k1,k2))

        seen = {}


        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        sorted_nums = sorted(seen, key=seen.get, reverse=True)
        
        return sorted_nums[:k]