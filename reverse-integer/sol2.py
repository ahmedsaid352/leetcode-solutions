class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(abs(x))
        x_str = int(x_str[::-1])
        if x < 0:
            x_str = -x_str
        if x_str > ((2**31)-1) or x_str < (-2**31):
            return 0
        else:
            return x_str