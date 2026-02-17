class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s = {}
        for num in s:
            if num not in hashmap_s:
                hashmap_s[num] = 1
            else:
                hashmap_s[num] += 1
        hashmap_t = {}
        for num in t:
            if num not in hashmap_t:
                hashmap_t[num] = 1
            else:
                hashmap_t[num] += 1
        if hashmap_s == hashmap_t:
            return True
        else:
            return False


        