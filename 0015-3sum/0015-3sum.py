class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            M = i + 1
            R = len(nums) - 1
            while M < R:
                Threesome = n + nums[M] + nums[R]
                if Threesome < 0:
                    M += 1
                elif Threesome > 0:
                    R -= 1
                else:
                    res.append([n , nums[M] , nums[R]])
                    M += 1
                    while nums[M] == nums[M - 1] and M < R:
                        M += 1
        return res                    
        
                
        