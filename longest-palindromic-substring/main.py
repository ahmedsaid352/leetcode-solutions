def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if s == s[::-1]:
        return s
    l = ''
    for i in range(len(s)):
        for j in range(len(s[i:])):
            if (s[i] == s[i+j]) and (s[i:i+j+1] == s[i:i+j+1][::-1]):
                if (len(l) < len(s[i:i+j+1])):
                    l = s[i:i+j+1]
    return l 


# test cases
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))

