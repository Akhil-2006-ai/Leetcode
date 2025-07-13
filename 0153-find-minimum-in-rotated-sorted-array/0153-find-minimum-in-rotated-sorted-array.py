class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        while L < R:
            Mid = (L + R) // 2
            if nums[Mid] > nums[R]:
                L = Mid + 1
            else:
                R = Mid

        return nums[L]



        