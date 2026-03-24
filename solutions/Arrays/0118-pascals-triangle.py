class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution=[]
        for i in range(numRows):
            temp=[1]
            answer=1
            for j in range(1,i+1):
                answer=int(answer*(i-j+1)/(j))
                temp.append(answer)
            solution.append(temp)

        return solution
