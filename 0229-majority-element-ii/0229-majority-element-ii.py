class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        res = []
        n = len(nums)
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        for key,value in hashmap.items():
            if value > n // 3:
                res.append(key)
        return res
        