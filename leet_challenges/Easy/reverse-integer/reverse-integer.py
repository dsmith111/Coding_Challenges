class Solution:
    def reverse(self, x: int) -> int:

        sign = ""
        x = str(x)

        if x[0]  == "-":
            sign = x[0]
            x = x[1:]

        x = x[::-1]
        x = sign + x
        x = int(x)

        if (x > (2**31)-1) or (x < (-2**31)):
            return 0

        return x
