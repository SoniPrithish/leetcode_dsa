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
                print("Yo",ind)
                break

        for i in range(n-1,-1,-1):
            if ind==-1:
                print("Hello Bhai")
                nums.reverse()
                return 0
            if nums[ind]<nums[i]:
                print("Yaha Tak Sahi hai")
                temp=nums[ind]
                print(temp,"Temp")
                nums[ind]=nums[i]
                print(nums,"Sahi")
                nums[i]=temp
                break
                print(nums,"hai")
        print(nums)
        print("Ye wala",nums[-(ind)+2:])
        nums[ind+1:]=nums[:ind:-1]
        print("Ye Change hoga",nums[-(ind)+2:][::-1])
        print(nums)
