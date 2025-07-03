# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        Low = 1
        High = n
        while Low <= High:
            Mid = (Low + High) // 2
            if guess(Mid) == -1:
                High = Mid - 1
            elif guess(Mid) == 1:
                Low = Mid + 1
            else:
                return Mid


    




