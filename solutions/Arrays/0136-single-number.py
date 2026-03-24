class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_set=set(nums)
        for i in num_set:
            if nums.count(i)==1:
                return i
        
        return -1
