class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        areas =[]
        ones = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ones.append((i,j))
        if len(ones) > 0:
            for one in ones:
                current_area = 0
                frontier = [one]
                visited = set()
                while len(frontier) > 0:
                    r,c = frontier.pop()
                    visited.add((r,c))
                    current_area+=1
                    for r,c in [(r,c) for r,c in [(r-1,c) , (r+1,c),(r,c-1),(r,c+1)] if (len(grid) > r >=0 and len(grid[0]) > c >= 0 ) and grid[r][c] == 1]:
                        if (r,c) not in visited:
                            frontier.append((r,c))
                areas.append(current_area)
            return max(areas)
        else:
            return 0