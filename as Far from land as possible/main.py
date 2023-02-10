class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        zeros =[]
        ones = []
        mn = 99999999999
        mx = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    zeros.append((i,j))
                else:
                    ones.append((i,j))
        if len(ones)==0 or len(zeros) == 0:
            return -1
        else:
            for zero in zeros:
                for one in ones:
                    if mn > (abs(zero[0]-one[0])+abs(zero[1]-one[1])):
                        mn = (abs(zero[0]-one[0])+abs(zero[1]-one[1]))
                if mx < mn:
                    mx = mn
                mn = 99999999999
            return mx