class Solution:
    def isValid(self, s: str) -> bool:
        leftP = '([{'
        rightP = ')]}'
        stack = []
        for m in s:
            if m in leftP:
                stack.append(m)
            if m in rightP:
                if not stack:
                    return False
                tmp = stack.pop()
                if m == ")" and tmp != "(":
                    return False
                if m == "]" and tmp != "[":
                    return False
                if m == "}" and tmp != "{":
                    return False
        return stack == []

if __name__ == '__main__':
    s = input()
    so = Solution()
    print(so.isValid(s))