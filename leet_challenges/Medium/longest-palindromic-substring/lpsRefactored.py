class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Expanding
        
        def expand(i, j):
            
            
            while(i >= 0 and j <len(s) and s[i] == s[j]):
                i -= 1
                j += 1
                
            
            return s[i+1 : j]
                
                
                
                
        # Main
        result = s[0]
        if len(s)%2 == 0:
            even = True
        else:
            even = False
        
        
        for i in range(len(s)):
            
            temp = expand(i, i)
            
            if len(temp) > len(result):
                result = temp
                

            temp = expand(i, i+1)

            
            if len(temp) > len(result):
                result = temp
                
        return result
            
            
        