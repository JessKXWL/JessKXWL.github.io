class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "":
            return 0
        s = s.strip()
        l1 = s.split(' ')
        return len(l1[-1])

if __name__ == '__main__':
    so = Solution()
    print(so.lengthOfLastWord("b a    "))