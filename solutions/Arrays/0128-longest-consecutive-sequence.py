class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=set(nums)
        best=0

        for num in d:
            if num-1 not in d:
                length=1
                curr=num
                while curr+1 in d:
                    length+=1
                    curr+=1
                best=max(best,length)
        return best
