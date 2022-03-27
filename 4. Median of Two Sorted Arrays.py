class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        temp = int(len(nums) / 2)
        
        if(len(nums) % 2 != 0):
            return nums[temp]
        else:
            temp -= 1
            return (nums[temp] + nums[temp + 1]) / 2