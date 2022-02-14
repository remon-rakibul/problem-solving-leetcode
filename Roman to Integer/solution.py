class Solution:
    def romanToInt(self, s: str) -> int:
        romanNum = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        minus = {'I':['V','X'], 'X':['L','C'], 'C':['D','M']}
        s = str(s)
        num = 0
        l = len(s)
        for i in range(l):
            if s[i] in minus and i+1 < l and s[i+1] in minus[s[i]]:
                num -= romanNum[s[i]]
            else:
                num += romanNum[s[i]]
        return num
