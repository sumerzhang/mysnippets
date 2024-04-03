class Solution(object):
  def quick_sort(self, nums):
    self.quick_sort_helper(nums, 0, len(nums) - 1)
    return nums
  def quick_sort_helper(self, nums, start, end):
    if start >= end:
      return
    pivot = nums[start]
    left, right = start, end
    while left <= right:
      while left <= right and nums[left] < pivot:
        left += 1
      while left <= right and nums[right] > pivot:
        right -= 1
      if left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    self.quick_sort_helper(nums, start, right)
    self.quick_sort_helper(nums, left, end)

# test
nums = [3, 2, 1, 5, 6, 4]
print(Solution().quick_sort(nums)) # [1, 2, 3, 4, 5, 6]
