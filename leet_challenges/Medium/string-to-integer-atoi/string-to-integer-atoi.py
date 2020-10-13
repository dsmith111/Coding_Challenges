class Solution:
    def myAtoi(self, s: str) -> int:

        compare = "0123456789-+"
        number = ""
        firstNumber = False
        sign = "+"
        for element in s:

            if (element == " ") and not firstNumber:
                continue

            if(element in "+-" and firstNumber):
                break

            if (element in compare):
                number += element
                firstNumber = True

            elif (not firstNumber):
                return 0

            else:
                break


        try:
            number = int(number)
        except:
            return 0

        if (number > (2**31) - 1):

            return ((2**31) - 1)

        elif (number < (-2**31)):

            return(-2**31)

        return int(number)


        
