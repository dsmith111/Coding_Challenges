class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        count = 0
        for number in nums:

            search = target - number
            nums[count] = None
            if search in nums:
                return [count, nums.index(search)]
            count += 1
