class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        net = 0
        instances = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        for instance in instances.keys():
            if instance in s:
                s = s.replace(instance,'')
                net += instances[instance]
        for letter in s:
            net += symbols[letter]
        return net
