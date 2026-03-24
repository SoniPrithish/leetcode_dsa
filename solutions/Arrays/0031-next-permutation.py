class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=-1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break

        for i in range(n-1,-1,-1):
            if ind==-1:
                nums.reverse()
                return 0
            if nums[ind]<nums[i]:
                temp=nums[ind]
                nums[ind]=nums[i]
                nums[i]=temp
                break

        nums[ind+1:]=nums[:ind:-1]
