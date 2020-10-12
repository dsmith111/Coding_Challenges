class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        
        pL = 0
        pR = len(s)-1
        longest = s[0]
        
        while pL < len(s):

            if s[pL] == s[pR]:
                temp_word = s[pL:pR+1]
                temp_reverse = temp_word[::-1]

                if (temp_word == temp_reverse) and (len(temp_word) > len(longest)):
                    longest = temp_word
                    #pL += 1
                    #pR = len(s)-1

            
            pR -= 1
            if(pR <= pL):
                pL += 1
                pR = len(s)-1
        return longest