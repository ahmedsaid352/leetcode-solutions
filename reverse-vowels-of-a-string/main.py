class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        s = list(s)  # Convert the string to a list

        # Two-pointer approach to swap vowels
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]  # Swap the vowels
                i += 1
                j -= 1
            elif s[i] in vowels:
                j -= 1
            else:
                i += 1

        return ''.join(s)  # Convert the list back to a string



        