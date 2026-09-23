class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        nums = sorted(nums)
        print(nums)

        max1 = nums[len(nums)-1]
        max2 = nums[len(nums)-2]

        min1 = 0
        min2 = 0

        min1 = nums[0]
        min2 = nums[1]

        return ((max1*max2) - (min1*min2))