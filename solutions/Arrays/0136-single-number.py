class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            freq[num] = freq.get(num, 0)+1
        for keys in freq:
            if freq[keys]==1:
                return keys
