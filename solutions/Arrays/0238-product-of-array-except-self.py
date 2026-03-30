class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefixprod=[1]*n
        postfixprod=[1]*n
        ans=[1]*n
        for i in range(1,n):
            prefixprod[i]=prefixprod[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            postfixprod[j]=postfixprod[j+1]*nums[j+1]
        for k in range(n):
            ans[k]=prefixprod[k]*postfixprod[k]
        return ans
