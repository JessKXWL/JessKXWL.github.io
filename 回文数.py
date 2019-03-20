class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)[::-1]
        s2 = str(x)[::1]
        if s == s2:
            return True
        else:
            return False



if __name__ == '__main__':
    s = input()
    num = int(s)