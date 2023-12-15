import re
class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        if len(password) < 8:
            return False
        
        for i in range(1, len(password)):
            if password[i- 1] == password[i]:
                return False
        
        if ((re.findall(r'[A-Z]',password)) and
            (re.findall(r'[a-z]',password)) and 
            (re.findall(r'[0-9]',password)) and 
            (re.findall(r'\W',password))):
            return True
        else:
            return False