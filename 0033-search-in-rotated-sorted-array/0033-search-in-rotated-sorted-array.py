class Solution:
    def search(self, nums: List[int], target: int) -> int:
        Low = 0
        High = len(nums) - 1

        
        while Low <= High:
            Mid = (Low + High) // 2
            if target == nums[Mid]:
               return Mid
            
            if nums[Low] <= nums[Mid]:
                if target > nums[Mid] or target < nums[Low]:
                    Low = Mid + 1
                else:
                    High = Mid - 1
            else:
                if target < nums[Mid] or target > nums[High]:
                    High = Mid - 1
                else:
                    Low = Mid + 1
        return -1

        

        
                