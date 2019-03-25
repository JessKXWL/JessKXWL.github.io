class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        # 查找数字
        index = -2
        flag = 0
        try:
            index = nums.index(target)
        except ValueError:
            for i in range(0,len(nums)):
                if nums[i] > target:
                    nums.insert(i, target)
                    index = i
                    flag = 1
                    break
            if flag == 0:
                index = len(nums)
        return index

if __name__ == '__main__':
    so = Solution()
    print(so.searchInsert([1,3,5,6], 5))