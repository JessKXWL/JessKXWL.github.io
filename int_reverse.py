# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21

# 方法一:
class Solution:
    def reverse(self, a):
        reverse_value = 0
        b = a
        if b>=0:
            while b != 0:
                m = b % 10
                b = b // 10
                reverse_value = reverse_value * 10 + m
            if reverse_value>2**31-1:
                return 0
            return reverse_value
        else:
            b = -a
            while b != 0:
                m = b % 10
                b = b // 10
                reverse_value = reverse_value * 10 + m
            if -reverse_value<-2**31:
                return 0
            return -reverse_value

# 方法二: 当为负数时修改为调用负函数且函数值为负
class Solution2:
    def reverse(self, a):
        reverse_value = 0
        b = a
        if b>=0:
            while b != 0:
                m = b % 10
                b = b // 10
                reverse_value = reverse_value * 10 + m
            if reverse_value>2**31-1:
                return 0
            return reverse_value
        else:
            return -self.reverse(-a)

        # return result if result_value <= 2**31-1 else 0

if __name__ == "__main__":
    s = Solution()
    m = s.reverse(120)
    print(m)
