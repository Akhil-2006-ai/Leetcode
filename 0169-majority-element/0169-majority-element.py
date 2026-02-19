class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
            if hashmap[nums[i]] > n // 2:
                return nums[i]
   


        