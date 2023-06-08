class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        for i in s:
            s=s+i
        if goal in s:
            return True
        return False
