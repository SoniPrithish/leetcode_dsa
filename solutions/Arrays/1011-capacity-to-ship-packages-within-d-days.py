class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap):
            d=1
            cap_used=0
            for w in weights:
                if cap_used+w>cap:
                    d+=1
                    cap_used=0
                cap_used+=w
            return d<=days
        left=max(weights)
        right=sum(weights)

        while(left<right):
            mid=(left+right)//2
            if can_ship(mid):
                right=mid
            else:
                left=mid+1
        return left
