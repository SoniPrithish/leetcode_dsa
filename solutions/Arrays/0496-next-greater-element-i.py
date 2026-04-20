class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        index_map= {n:-1 for n in nums1}
        
        for i in range(len(nums2)):
            curr=nums2[i]
            while stack and curr>stack[-1]:
                val=stack.pop()
                index_map[val]=nums2[i]
            if curr in index_map:
                stack.append(curr)
        return [i for i in index_map.values()]
