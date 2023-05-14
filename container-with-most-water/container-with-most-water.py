class Solution(object):
    def maxArea(self,height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j = len(height) - 1
        w = j 
        max_area =0
        while i < j :
            if height[i] > height[j]:
                h = height[j]
                j-=1
            else:
                h = height[i]
                i+=1
            current_area = h * w
            if current_area > max_area :
                max_area = current_area
            w-=1
        return max_area