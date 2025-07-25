class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i,num in enumerate(nums):
            if num in hashmap and abs(hashmap[num] - i) <= k:
                return True
            hashmap[num] = i
        return False


        