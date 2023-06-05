class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ct_zero=nums.count(0)
        for i in range(ct_zero):
            nums.remove(0)
            nums.append(0)
