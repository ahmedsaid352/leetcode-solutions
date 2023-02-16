class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    current_area = 0
                    frontier = [(i,j)]
                    visited.add((i,j))
                    while frontier:
                        r,c = frontier.pop()
                        current_area+=1
                        for r, c in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (len(grid) > r >=0 and len(grid[0]) > c >= 0 ) and (grid[r][c] == 1) and ((r,c) not in visited):
                                frontier.append((r,c))
                                visited.add((r,c))
                    if max_area < current_area:
                        max_area = current_area
        return max_area