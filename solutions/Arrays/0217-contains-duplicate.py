class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num2=set(nums)
        if len(num2)==len(nums):
            return False
        else :
            return True
