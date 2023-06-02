class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Move all positive integers to their corresponding indices
        # For example, the number 3 should be placed at index 2 (3-1)
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                # Swap the current number to its correct position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        # Find the first index where the number is not equal to its index + 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

    # If all numbers are in their correct positions, return the next positive integer
        return len(nums) + 1
