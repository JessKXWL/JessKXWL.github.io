class Solution: # 遍历nums, 如果数组中有重复的, 则出队。否则下标加1
    def removeDuplicates(self, nums: list) -> list:
        index = 0
        while index<len(nums)-1:
            if nums[index] == nums[index+1]:
                nums.pop(index)
            else:
                index = index + 1
        return nums

class Solution1: # 遍历整个数组, 如果下标小于1 或者 该数值在之前没有重复，则下标加1.
    def removeDuplicates(self, nums: list) -> list:
        index = 0
        for num in nums:
            if index<1 or num != nums[index-1]:
                nums[index] = num
                index = index + 1
        return index

if __name__ == '__main__':
    l1 = [0,0,1,1,1,2,2,3,3,4]
    so = Solution1()
    print(so.removeDuplicates(l1))