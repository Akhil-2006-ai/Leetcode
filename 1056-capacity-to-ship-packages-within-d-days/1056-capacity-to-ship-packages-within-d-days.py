class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        Mincapacity = max(weights)
        Maxcapacity = sum(weights)
        Res = Maxcapacity

        def capacity(cap):
            ship  , currentcapacity = 1,cap
            for weight in weights:
                if currentcapacity - weight < 0:
                    ship += 1
                    currentcapacity = cap
                currentcapacity -= weight
            return ship <= days

        while Mincapacity <= Maxcapacity:
            
            cap = (Mincapacity + Maxcapacity) // 2
            if capacity(cap):
                Maxcapacity = cap - 1
                Res = min(Res,cap)
            else:
                Mincapacity = cap + 1
        return Res





