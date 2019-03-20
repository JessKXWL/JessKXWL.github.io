class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        flag = 0
        for i in range(0,len(s)):
            if flag == 1:
                flag = 0
                continue
            elif i+1 < len(s) and s[i] == 'I' and s[i+1] == 'V':
                num = num + 4
                flag = 1
                continue
            elif i+1 < len(s) and s[i] == 'I' and s[i+1] == "X":
                num = num + 9
                flag = 1
                continue
            elif i+1 < len(s) and s[i] == 'X' and s[i+1] == "L":
                num = num + 40
                flag = 1
                continue
            elif i+1 < len(s) and s[i] == 'X' and s[i+1] == "C":
                num = num + 90
                flag = 1
                continue
            elif i+1 < len(s) and s[i] == 'C' and s[i+1] == "D":
                num = num + 400
                flag = 1
                continue
            elif i+1 < len(s) and s[i] == 'C' and s[i+1] == "M":
                num = num + 900
                flag = 1
                continue
            else:
                num = num + map[s[i]]
                flag = 0
                continue
        return num

if __name__ == '__main__':
    s = input()
    so = Solution()
    print(so.romanToInt(s))