class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split()
        reversewords = s[::-1]
        return len(reversewords[0])
        