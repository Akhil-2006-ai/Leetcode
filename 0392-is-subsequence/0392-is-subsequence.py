class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        L , R = 0 , 0
        while L < len(s) and R < len(t):
            if s[L] == t[R]:
                L += 1
                R += 1
            else:
                R += 1
        if L == len(s):
            return True
        return False
