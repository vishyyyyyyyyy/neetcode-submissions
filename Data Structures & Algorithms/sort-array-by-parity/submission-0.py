class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr= []
        for num in nums:
            if num % 2 ==0:
                arr.append(num)
        
        for num in nums:
            if num % 2 == 1:
                arr.append(num)

        return arr