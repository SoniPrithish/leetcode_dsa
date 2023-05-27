class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        max_length = 0

        # Count the frequency of each number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Iterate over the numbers and check for harmonious subsequences
        for num in freq:
            if num + 1 in freq:
                length = freq[num] + freq[num + 1]
                max_length = max(max_length, length)

        return max_length
