class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z=0
        o=0
        t=0
    
        for i in range(len(nums)):
            if(nums[i])==0:
                z+=1
            elif (nums[i])==1:
                o+=1
            elif (nums[i])==2:
                t+=1

        o=o+z
        t=t+o
        print("zero",z,"one",o,"two",t)
        for i in range(len(nums)):
            if i<z:
                nums[i]=0
            elif i<o:
                nums[i]=1
            elif i<t:
                nums[i]=2
