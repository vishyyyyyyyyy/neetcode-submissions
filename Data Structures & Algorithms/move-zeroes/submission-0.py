class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        arr=[]
        for i in range(len(nums)):
            if nums[i] == 0:
                count +=1
            else:
                arr.append(nums[i])

        for i in range(count):
            arr.append(0)

          
        nums[:] = arr