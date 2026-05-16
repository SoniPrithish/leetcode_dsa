class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(arr):
            prev2=0
            prev1=0

            for i in range(len(arr)):
                take=arr[i]+prev2
                nottake=prev1
                curr=max(take,nottake)
                prev2=prev1
                prev1=curr
            return prev1
        if len(nums)==1:
            return nums[0]
        return max(solve(nums[1:]),solve(nums[:-1]))
