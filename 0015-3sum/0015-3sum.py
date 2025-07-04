class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []

        for i , a in enumerate(nums):
            if i > 0 and  a == nums[i - 1]:
                continue


            L = i + 1
            R = len(nums) - 1
           


            while L < R:
                Threesum =  a + nums[L] + nums[R] 
                if Threesum > 0:
                   R -= 1
                elif Threesum < 0:
                   L += 1
                else:
                   sol.append([a , nums[L] , nums[R]])
                   L += 1
                   while nums[L] == nums[L - 1] and L < R:
                    L += 1
        return sol
            


