# 一个数组全部是数字，怎么尽可能快的找到三个数字之和是10,用python实现
# 要在一个数组中尽可能快地找到三个数字之和等于10，
# 你可以使用一种称为"三数之和"的算法。
# 这个算法的基本思想是首先对数组进行排序，
# 然后使用双指针技巧来查找三个数字的组合。
def three_sum_to_10(nums):
    # 首先对数组进行排序
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 10:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif total < 10:
                left += 1
            else:
                right -= 1

    return result

# 示例输入
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = three_sum_to_10(nums)
print(result)
