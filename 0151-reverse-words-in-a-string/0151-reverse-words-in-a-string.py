class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        reversewords = s[::-1]
        return " ".join(reversewords)
        