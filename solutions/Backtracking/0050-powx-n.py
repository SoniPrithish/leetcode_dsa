class Solution:
    def solve(self,x:float, n:int):
        if(n==0):
            return 1.0
        if(n==1):
            return x
        if(n%2==0):
            return self.solve(x*x,n/2)
        
        return x*self.solve(x,n-1)

    def myPow(self, x: float, n: int) -> float:
        if(n<0):
            return 1.0/self.solve(x,-n)
        
        return self.solve(x,n)
