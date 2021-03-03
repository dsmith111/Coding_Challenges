class Solution:
    def romanToInt(self, s: str) -> int:
        romanDictionary = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        count = 0
        lastNumber = 0
        
        for numeral in s:
            currentNumber = romanDictionary[numeral]
            if(currentNumber == lastNumber * 5 or currentNumber == lastNumber * 10 ):
                count += currentNumber - (lastNumber  * 2)
                lastNumber = romanDictionary[numeral]    
                continue
            count += currentNumber
            lastNumber = romanDictionary[numeral]

        return count