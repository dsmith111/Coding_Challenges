class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        rl = []
        for i in range(len(nums)):
            if (i == 0):
                rl.append(nums[0])
                continue
                
            rl.append(nums[i] + rl[i-1])
            
        return rl