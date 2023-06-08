class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_s = s[::-1].split(" ")
        ans = ''
        for i in range(len(reversed_s) - 1, -1, -1):
            ans += reversed_s[i] + ' '
        
        return ans.rstrip()
