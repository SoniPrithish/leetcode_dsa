class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_score=(max(nums)-k)-(min(nums)+k)
        if min_score<0:
            return 0
        return(min_score)
