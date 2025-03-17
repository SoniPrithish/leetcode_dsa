class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp=0
        maxi=0
        for i in nums:
            if i==1:
                temp+=1
            maxi=max(temp,maxi)
            if(i==0):
            
                temp=0
        return maxi
