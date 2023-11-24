class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        i = 0
        j = len(piles) - 1
        result = 0
        while i < j:
            result += piles[j - 1]
            j-=2
            i+=1
        return result