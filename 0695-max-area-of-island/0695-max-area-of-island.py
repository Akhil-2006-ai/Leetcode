class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , columns = len(grid) , len(grid[0])
        num_islands = 0
        visited = set()

        if not grid:
            return 0

        def bfs(r,c):
           q = collections.deque()
           visited.add((r,c))
           q.append((r,c))
           area = 1

           while q:
               row , col = q.popleft()
               directions = [[-1,0],[1,0],[0,1],[0,-1]]

               for dr , dc in directions:
                    r , c = (row + dr) , (col + dc)
                    if (r in range(rows) and c in range(columns) and grid[r][c] == 1 and (r,c) not in visited):
                       visited.add((r,c))
                       q.append((r,c))
                       area += 1
           return area




        max_area = 0
        for r in range(rows):
           for c in range(columns):
               if grid[r][c] == 1 and (r , c) not in visited:
                    
                    max_area = max(max_area , bfs(r , c))
        return max_area
