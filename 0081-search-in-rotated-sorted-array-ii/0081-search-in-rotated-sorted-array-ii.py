class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        Low = 0
        High = len(nums) - 1
        while Low <= High:
            Mid = (Low + High) // 2
            if nums[Mid] == target:
                return True
            if nums[Low] < nums[Mid]:
                if nums[Low] <= target < nums[Mid]:
                    High = Mid - 1
                else:
                    Low = Mid + 1
            elif nums[Low] > nums[Mid]:
                if nums[Mid] < target <= nums[High]:
                    Low = Mid + 1
                else:
                    High = Mid - 1
            else:
                Low += 1
        return False