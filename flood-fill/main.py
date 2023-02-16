class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        start = image[sr][sc]
        frontier = [(sr,sc)]
        visited = set()
        while len(frontier) > 0:
            r,c = frontier.pop()
            visited.add((r,c))
            image[r][c] = color
            for r,c in [(r,c) for r,c in [(r-1,c) , (r+1,c),(r,c-1),(r,c+1)] if (r >=0 and c >= 0 and r < len(image) and c < len(image[0])) and image[r][c] == start]:
                if (r,c) not in visited:
                    frontier.append((r,c))
        return image