class Solution:
    def decodeString(self, s: str) -> str:
        n=len(s)
        sol=[]
        curr_str=""
        curr_num=0
        for ch in s:
            if ch.isdigit():
                curr_num=curr_num*10+int(ch)
            elif (ch=="["):
                sol.append((curr_str,curr_num))
                curr_str=""
                curr_num=0
            elif (ch=="]"):
                prev_str,num=sol.pop()
                curr_str=prev_str + curr_str*num
            else:
                curr_str+=ch
        return curr_str
