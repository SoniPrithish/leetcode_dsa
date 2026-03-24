class Solution:
    def fib(self, n: int) -> int:
        n1=0
        n2=1
        sum=0
        if n==1:
            return 1
        for i in range(0,n-1):
            sum=n1+n2
            n1=n2
            n2=sum
        return sum
