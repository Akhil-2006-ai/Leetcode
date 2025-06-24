from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i+1,n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                L = j + 1
                R = n - 1
                while L < R:
                    Foursum = nums[i] + nums[j] + nums[L] + nums[R]
                    if Foursum < target:
                        L += 1
                    elif Foursum > target:
                        R -= 1
                    else:
                        res.append([nums[i] ,nums[j] , nums[L] , nums[R]])

                        while L < R and nums[L] == nums[L + 1]:
                            L += 1
                        
                        while L < R and nums[R] == nums[R - 1]:
                            R -= 1
                        
                        L += 1
                        R -= 1
        return res
                        

