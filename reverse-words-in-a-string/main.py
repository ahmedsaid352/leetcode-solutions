class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        reversed_str = ''
        for word in words[::-1]:
            if len(word.strip()) > 0:
                reversed_str = reversed_str + word.strip() + ' '

        return reversed_str.strip() 
        