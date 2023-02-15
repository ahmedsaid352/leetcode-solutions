class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        streak = []
        letters = []
        if len(s)> 1:
            for letter in s:
                if letter not in letters:
                    letters.append(letter)
                    counter+=1
                else:
                    streak.append(counter)
                    index_duplicated = letters.index(letter)
                    counter -= (index_duplicated)
                    letters = letters[index_duplicated+1:]
                    letters.append(letter)
            streak.append(counter)
            return max(streak)
        else:
            return len(s)