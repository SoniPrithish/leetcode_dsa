class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]

        def backtracking(start,path,remaining):
            if(remaining==0):
                result.append(path[:])
                return
            
            #invalid path
            if remaining< 0:
                return 
            
            for i in range(start,len(candidates)):

                #choose:
                path.append(candidates[i])

                #explore:
                backtracking(i,path,remaining-candidates[i])

                #undo
                path.pop()
        backtracking(0,[],target)
        return result
