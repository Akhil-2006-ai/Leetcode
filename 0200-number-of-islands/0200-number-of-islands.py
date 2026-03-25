class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows , columns = len(grid) , len(grid[0])
        visited = set()
        num_islands = 0

        def bfs(row , col):
            q = collections.deque()
            visited.add((row,col))
            q.append((row,col))

            while q:
                row , col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
               
                for dr,dc in directions:
                    r ,c = (row + dr) , (col + dc)
                    if (r in range(rows) and c in range(columns) and grid[r][c] == "1" and (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))



        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r , c) not in visited:
                    bfs(r,c)
                    num_islands += 1
        return num_islands



