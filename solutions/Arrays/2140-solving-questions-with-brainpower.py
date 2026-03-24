class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp=[0]*(n+1)
        
        for i in range(n-1,-1,-1):
            points,brainpower=questions[i]
            next_index=i+brainpower+1
        
            solve=points
            if(next_index< n):
                solve+=dp[next_index]
            nottake=dp[i+1]

            dp[i]=max(solve,nottake)
        return dp[0]
