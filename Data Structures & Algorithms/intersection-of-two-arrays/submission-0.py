class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        seen = set(nums1)
        seen2 = set(nums2)
        newseen= []

        for num in seen2:
            if num in seen:
                newseen.append(num)
            else:
                continue

        return (newseen)