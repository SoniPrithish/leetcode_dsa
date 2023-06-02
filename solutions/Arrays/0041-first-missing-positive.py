class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 1
        indicator = []
        for i in range(0, n + 1):
            indicator.append(0)
        for i in range(0, n):
            if nums[i] >= 0 and nums[i] <= n:
                indicator[nums[i]] = 1
                
        for i in range(1, n + 1):
            if indicator[i] == 0:
                return i
        
        return n + 1
