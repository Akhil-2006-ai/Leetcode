class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        totalsum = sum(nums)
        for i in range(len(nums)):
            if leftsum == totalsum - nums[i] - leftsum:
                return i
            leftsum += nums[i]
        return -1