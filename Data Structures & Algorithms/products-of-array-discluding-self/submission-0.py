class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        length = len(nums)

        left = 1
        for num in nums:
            arr.append(left)
            left *= num

        right = 1
        i = length - 1
        for num in nums[::-1]:
            arr[i] = arr[i] * right
            i -=1
            right *= num

        return arr