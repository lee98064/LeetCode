class Solution1(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, value in enumerate(nums):
           remaining = target - nums[i]
           
           if remaining in seen:
               return [i, seen[remaining]]
            
           seen[value] = i


class Solution2(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            save = nums.copy()
            n = save.pop(i)
            if(target - n in save):
                ans = [i , save.index(target - n) + 1]
                break
        return(ans)


a1 = Solution1().twoSum([3,2,4],6)
a2 = Solution2().twoSum([3,2,4],6)
print(a1)
print(a2)
