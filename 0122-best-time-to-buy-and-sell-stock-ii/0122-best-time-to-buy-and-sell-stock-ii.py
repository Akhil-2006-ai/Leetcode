class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        maxprofit = []
        for R in range(1,len(prices)):
            if prices[L] < prices[R]:
                maxprofit.append(prices[R] - prices[L])
                L = R
            else:
                L = R
        if maxprofit:
            return sum(maxprofit)
        else:
            return 0


        