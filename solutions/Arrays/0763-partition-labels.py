class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap={} # SToring last appearance's index
        for i,c in enumerate(s):
            hashmap[c]=i
        result=[]
        size=0
        end=0
        for i,c in enumerate(s):
            size+=1
            end=max(end,hashmap[c])
            if i==end:
                result.append(size)
                size=0
        return result
