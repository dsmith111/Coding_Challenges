class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        rl = []
        for i, number in enumerate(nums):
            if (i == 0):
                rl.append(number)
                continue
                
            rl.append(number + rl[i-1])
            
        return rl