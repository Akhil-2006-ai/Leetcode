class Solution:
    def reverseWords(self, s: str) -> str:
       s = s.strip()
       words = s.split()
       reversedwords = words[::-1]
       return " ".join(reversedwords)