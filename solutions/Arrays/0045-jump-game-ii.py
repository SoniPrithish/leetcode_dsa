class Solution:
    def jump(self, nums: List[int]) -> int:
        minjumps=0
        farthest=0
        currend=0
        n=len(nums)

        for i in range(n-1):
            farthest=max(farthest,i+nums[i])
            if i==currend:
                minjumps+=1
                currend=farthest
                
        return minjumps
