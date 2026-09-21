class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        array = [0]
        count = 0
        for num in nums:
            if num == 1:
                count +=1
            else:
                array.append(count)
                count = 0
        array.append(count)
        return (max(array))