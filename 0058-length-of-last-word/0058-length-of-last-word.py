class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = s.split()
        reversewords = words[::-1]
        return len(reversewords[0])
        