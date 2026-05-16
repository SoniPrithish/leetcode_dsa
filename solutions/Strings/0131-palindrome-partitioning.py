class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result=[]

        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start,path):
            if start==len(s):
                result.append(path[:])
                return
            #try every cut

            for end in range(start,len(s)):
                substring=s[start:end+1]

                #check if palindrome and continue only if palindrome
                if is_palindrome(substring):
                    path.append(substring)

                    #explore
                    backtrack(end+1,path)

                    #undo
                    path.pop()
        backtrack(0,[])
        return result
