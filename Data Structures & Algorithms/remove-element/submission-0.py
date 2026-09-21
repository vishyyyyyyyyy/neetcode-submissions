class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val] #[:] <- makes it use the original arr passed in instead of making a new copy
        return(len(nums))