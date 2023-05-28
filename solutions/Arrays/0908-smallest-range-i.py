class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_score=(max(nums)-k)-(min(nums)+k)
        return max(0,min_score)
