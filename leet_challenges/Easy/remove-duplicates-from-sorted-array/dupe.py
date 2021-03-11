class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prevNumber = None
        i = 0
        
        while i < len(nums):
            if(i == 0):
                prevNumber = nums[i]
                i += 1
                continue
            if(nums[i] == prevNumber):
                nums.pop(i)
                continue
            prevNumber = nums[i]
            i += 1
            
        return len(nums)
            