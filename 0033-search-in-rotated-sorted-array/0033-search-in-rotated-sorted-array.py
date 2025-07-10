class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            Mid = (L + R) // 2
            if target == nums[Mid]:
                return Mid
            if nums[L] <= nums[Mid]:
                if target > nums[Mid] or target < nums[L]:
                    L = Mid + 1
                else:
                    R = Mid - 1
            else:
                if target < nums[Mid] or target > nums[R]:
                    R = Mid - 1
                else: 
                    L = Mid + 1
                
        return -1

        