class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        index = 0
        while index<len(nums):
            if nums[index] == val:
                nums.pop(index)
            else:
                index = index+1
        print(nums)
        return len(nums)

class Solution1(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == '__main__':
    so = Solution()
    so.removeElement([3,2,2,3],3)