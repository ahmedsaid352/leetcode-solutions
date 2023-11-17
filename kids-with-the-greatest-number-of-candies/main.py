class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        greatest = 0
        for n in candies:
            if n > greatest:
                greatest = n
        
        ref = greatest - extraCandies
        result = []
        for i in candies:
            if i >= ref:
                result.append(True)
            else:
                result.append(False)
        
        return result