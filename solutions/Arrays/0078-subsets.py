class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(index,current):
            if index==len(nums):
                result.append(current[:])
                return
            #include
            current.append(nums[index])
            backtrack(index+1,current)

            #backtrack
            current.pop()

            #Exclude
            backtrack(index+1,current)
        backtrack(0,[])
        return result
