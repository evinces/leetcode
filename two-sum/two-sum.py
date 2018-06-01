"""Two sum

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

"""


# O(n^2)
class Solution1:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# O(n)
class Solution2:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_dict = {}
        for index, value in enumerate(nums):
            nums_dict[value] = index

        for index, value in enumerate(nums):
            difference = target - value
            if difference in nums_dict and nums_dict[difference] != index:
                return [index, nums_dict[difference]]
