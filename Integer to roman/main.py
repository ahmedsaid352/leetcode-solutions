class Solution(object):
    def intToRoman(self, num):
        s = ''
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for i in range(len(values)):
            if num >= values[i]:
                delta = int(num/values[i])
                num-=delta*values[i]
                s+=delta*symbols[i]
        return s