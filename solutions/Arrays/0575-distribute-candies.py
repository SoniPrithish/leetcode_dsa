class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s1=set(candyType)
        max_candies=int(len(candyType)/2)
        if max_candies>=len(s1):
            return len(s1)
        else:
            return max_candies
