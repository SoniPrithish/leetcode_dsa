class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[float('inf')]*(len(days)+1)
        n=len(days)
        dp[n]=0

        for i in range(n-1,-1,-1):

            #option1
            option1=costs[0]+dp[i+1]
            
            #option2
            k=i
            while(k<n and days[k]<days[i]+7):
                k+=1
            option2=costs[1]+dp[k]

            #OPTION3
            k=i
            while(k<n and days[k]<days[i]+30):
                k+=1
            option3=costs[2]+dp[k]

            dp[i]=min(option1,min(option2,option3))
        return dp[0]
