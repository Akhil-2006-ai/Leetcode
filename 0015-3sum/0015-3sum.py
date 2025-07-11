class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
       
        
        
        res = []
        
        for i , n in enumerate(nums):
            if i > 0  and nums[i] == nums[i - 1]:
                continue
            k = i + 1
            j = len(nums) - 1
            while k < j:
              Threesome = n + nums[k] + nums[j]
              if Threesome < 0:
                k += 1
              elif Threesome > 0:
                j -= 1
              else:
                res.append([n , nums[k] , nums[j]])
                k += 1
                while nums[k] == nums[k - 1] and k < j:
                    k += 1
        return res



            
            

        