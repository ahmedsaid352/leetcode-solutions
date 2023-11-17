class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        short_str = ''

        if len(str1) > len(str2):
            short_str = str2
        else:
            short_str = str1
        
        n = len(short_str)

        while n > 0:
            if (set(str1.split(short_str[:n+1]))  == {""}) and (set(str2.split(short_str[:n+1]))  == {''}) :
                return short_str[:n+1]

            n-=1
        
        return ""
        
        n = len(short_str)

        while n > 0:
            try:
                if (len(set(str1.split(short_str[:n+1])) == 1)) and (len(set(str2.split(short_str[:n+1])) == 1)) :
                    return short_str[:n+1]
            except:
                pass

            n-=1
        
        return ""