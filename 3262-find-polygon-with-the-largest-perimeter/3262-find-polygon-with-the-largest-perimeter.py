class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        total = sum(nums)
        nums.sort()
        for i in range(len(nums) - 1 , -1 , -1):
            if total - nums[i] > nums[i]:
                return total
            total -= nums[i]
        return -1
          


        