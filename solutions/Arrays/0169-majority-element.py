
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=nums[0]
        ct=1
        for i in range(1,len(nums)):
            if ct==0:
                maj=nums[i]
                ct+=1
            elif(nums[i]==maj):
                ct+=1
            else:
                ct-=1
        return maj
