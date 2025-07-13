class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = list(enumerate(nums))
        nums.sort(key = lambda num: num[1])
        print(nums)
        l=0
        r=len(nums)-1
        while r>l:
            if nums[l][1]+nums[r][1] == target:
                return [nums[l][0],nums[r][0]]
            elif nums[l][1]+nums[r][1] > target:
                r-=1
            else:
                l+=1
        
        