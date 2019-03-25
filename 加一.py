class Solution:
    def plusOne(self, digits: list) -> list:
        num = ''.join(str(i) for i in digits)
        num = int(num)
        num = num + 1
        l2 = list(str(num))
        l3 = []
        for i in l2:
            l3.append(int(i))
        return l3
if __name__ == '__main__':
    so = Solution()
    print(so.plusOne([1,2,3]))