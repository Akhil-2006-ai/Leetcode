class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        Low = 1
        High = max(piles)
        Res = []
        

        while Low <= High:
            K = (Low + High) // 2
            Hours = 0
            for p in piles:
                Hours += math.ceil( p / K)
            if Hours <= h:
                Res.append(K)
                High = K - 1
            else:
                Low = K + 1

        return min(Res)

                







        


        
        