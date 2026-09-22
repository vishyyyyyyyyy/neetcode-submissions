class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        newnum = []
        for num in nums:
            newnum.append(num)

        return (nums+newnum)