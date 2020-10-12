class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        i, j = (0, 0)
        holding_array = [""]*numRows

        reverse = False
        if numRows == 1:
            return s
        
        for letter in s:

            holding_array[i] += letter 
            
            if reverse == False:
                i += 1
            
            else:
                i -= 1
            
            if i>= numRows:
                i -= 2
                reverse = True
                
            elif i <0 and reverse == True:
                i = 1
                reverse = False
                
        return "".join(holding_array)