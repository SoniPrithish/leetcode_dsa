class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        min_score=(nums[len(nums)-1]-k)-(nums[0]+k)
        if min_score<0:
            return 0
        return(min_score)
