class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer=[]
        if len(nums1)<=len(nums2):
            for num in nums1:
                print(num,"-idhar")
                if num in nums2:
                    answer.append(num)
                    nums2.remove(num)
        else:
            
            for num in nums2:
                print(num,"-udhar")
                if num in nums1:
                    answer.append(num)
                    nums1.remove(num)
                    print("Nums1->",nums1,"Nums2->",nums2)
            
                
        return answer
