class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        nums=[]
        for num,ct in c.items():
            if ct==2:
              nums.append(num)
        return nums
