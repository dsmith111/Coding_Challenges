class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        logic_array = []
        thresh = max(candies)
        #for candy in candies:
        #    if(candy+extraCandies >= thresh):
        #        logic_array.append(True)
        #    else:
        #        logic_array.append(False)
        
        logic_array = list(map(lambda candy: (candy+extraCandies) >= thresh, candies))
        return logic_array

    