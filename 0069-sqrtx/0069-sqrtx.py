class Solution:
    def mySqrt(self, x: int) -> int:
        L = 0
        R = x
        Res = 0
        while L <= R:
            Mid = (L + R ) // 2
            
            
            if Mid**2 > x:
                R = Mid - 1
            elif Mid**2 < x:
                L = Mid + 1
                Res = Mid
            else:
                return Mid
        return Res
        


        
            
        