class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count= Counter(nums)
        nums= sorted(list(set(nums)))
        earn1=0
        earn2=0

        for i in range(0,len(nums)):
            currearn=nums[i]*count[nums[i]]
            if(i>0 and nums[i]-1==nums[i-1]):
                temp=earn1
                earn1=max(currearn+earn2,earn1)
                earn2=temp
            else:
                temp=earn1
                earn1=currearn+earn1
                earn2=temp
        return earn1
