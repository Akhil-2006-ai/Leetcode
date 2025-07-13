class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        set(nums)
        L = 0
        R = len(nums) - 1
        while L <= R:
            Mid = (L + R) // 2
            if target < nums[Mid]:
                R = Mid - 1
            elif target > nums[Mid]:
                L = Mid + 1
            else:
                return True
        return False

        