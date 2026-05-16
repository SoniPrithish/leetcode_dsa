class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]

        def backtrack(path,open_count,close_count):
            if len(path)==2*n:
                result.append("".join(path))
                return
            #Add opening bracket
            if open_count<n:
                path.append("(")
                #explore
                backtrack(path,open_count+1,close_count)
                path.pop()
            #Add closing bracket
            if close_count<open_count:
                path.append(")")
                backtrack(path,open_count,close_count+1)
                path.pop()
        backtrack([],0,0)
        return result
