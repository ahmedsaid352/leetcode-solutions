class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction = sorted(satisfaction)
        like_time_coef = 0
        n = len(satisfaction)
        for i in range(n):
            current = 0
            c = 1
            for j in range(i,n):
                current+= (c * satisfaction[j])
                c+=1
            if current > like_time_coef:
                like_time_coef = current
        return like_time_coef 
        