class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == 0:
            return 0
        if haystack == 0:
            return 0
        return haystack.find(needle)

# KMP 算法


if __name__ == '__main__':
    so = Solution()
    print(so.strStr("aaaaa", "bba"))