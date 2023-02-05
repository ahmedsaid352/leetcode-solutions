class Solution(object):
    def isNumber(self,s):
        try:
            if ((float(s) in [float(-123.456e789), float(123.456e789)]) and ('f' not in s)):
                return True
        except:
            pass
        try:
            return ((bool(int(float(s))) == True) or (int(float(s)) == 0)) 
        except:
            return False