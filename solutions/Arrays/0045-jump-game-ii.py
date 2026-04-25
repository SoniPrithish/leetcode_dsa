class Solution:
    def jump(self, nums: List[int]) -> int:
        inf=float('inf')
        n=len(nums)
        last=n-1
        jumps=[inf]*n
        jumps[last]=0
        

        for i in range(n-2,-1,-1):
            reqd=last-i
            curr_jump=nums[i]
            if curr_jump>=reqd:
                jumps[i]=1
            else:
                jumps[i] = 1 + min((jumps[i + j] for j in range(1, curr_jump + 1) if i + j < n), default=inf)
        return jumps[0]
