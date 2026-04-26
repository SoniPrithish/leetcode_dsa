import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        totalbanana=sum(piles)
        left,right=int(totalbanana/h) if int(totalbanana/h)>0 else 1,max(piles)

        while(left<right):
            mid=(left+right)//2
            hour=sum(math.ceil(p/mid) for p in piles)

            if hour<=h:
                right=mid
            else:
                left=mid+1
        return left
