class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            Mid = (L + R) // 2
            if target == nums[Mid]:
                return Mid
            elif target > nums[Mid]:
                L += 1
            else:
                R -= 1
        return L
            