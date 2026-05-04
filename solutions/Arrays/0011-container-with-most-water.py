class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left,right=0,n-1
        most_water=0
        while(left<right):
            water=min(height[left],height[right])*(right-left)
            most_water=max(most_water,water)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return most_water
