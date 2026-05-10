class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*(2*n-1)
        ans[:n]=nums[:]
        ans[n:]=nums[::-1]
        return ans
