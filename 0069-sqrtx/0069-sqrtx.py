class Solution:
    def mySqrt(self, x: int) -> int:
        L = 0
        R = x
        res = 0
        while L <= R:
            Mid = (L + R) // 2
            if Mid**2 < x:
                L= Mid + 1
                res = Mid
            elif Mid**2 > x:
                R  = Mid - 1
            else:
                return Mid
        return res




        