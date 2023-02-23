class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            sign = 1
        else:
            sign = -1
        x = str(abs(x))
        ans = 0
        for i in range(len(x)):
            ans += int(x[i])*(10**i)
        if (ans * sign) >= -2**31 and (ans * sign) <= ((2**31)-1):
            return ans * sign
        else:
            return 0