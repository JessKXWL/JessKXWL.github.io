import os


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        return os.path.commonprefix(strs)


class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or strs[0][i] != str[i]:
                    return strs[0][:i]
        return strs[0]

class Solution2:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        dp = [strs[0]] * len(strs)
        for i in range(1, len(strs)):
            while not strs[i].startswith(dp[i-1]):# 若不是以dp[i-1]开头的, 就去后面一位
                dp[i-1] = dp[i-1][:-1]
            dp[i] = dp[i-1]
        return dp[-1]

if __name__ == '__main__':
    s = input()
    # print(s)
    l = s.split(',')
    # print(l)
    so = Solution2()
    print(so.longestCommonPrefix(l))