class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        fib = [0,1]
        i = 2
        while i <=n:
            temp = fib[1]
            fib[1] = fib[0] + fib[1]
            fib[0] = temp
            i += 1

        return fib[1]
        
        