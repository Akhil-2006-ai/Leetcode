class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmaps = {}
        hashmapt = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in hashmaps:
                hashmaps[s[i]] += 1
            else:
                hashmaps[s[i]] = 1
       
        
            if t[i] in hashmapt:
                hashmapt[t[i]] += 1
            else:
                hashmapt[t[i]] = 1
        if hashmaps == hashmapt:
            return True
        else:
            return False
        
         