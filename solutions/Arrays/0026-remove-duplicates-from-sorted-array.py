class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        # Initialize the index for placing unique elements
        unique_index = 1
    
        # Start from the second element and compare with the previous one
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_index] = nums[i]
                unique_index += 1
    
        # Return the length of the array without duplicates
        return unique_index
