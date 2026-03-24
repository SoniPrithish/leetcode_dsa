class Solution:
    def tribonacci(self, n: int) -> int:
        n1=0
        n2=1
        n3=1
        if n==1 or n==2:
            return 1
        sum=0
        for i in range(2,n):
            sum=n1+n2+n3
            n1=n2
            n2=n3
            n3=sum
        return sum
