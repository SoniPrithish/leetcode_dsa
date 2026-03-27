class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums=nums1[0:m]
        i=0
        j=0
        k=0
        if(n==0):
            return
        if(m==0):
            nums1[0]=nums2[0]
        while(k< len(nums1)):
            if(i<m and j>=n):
                nums1[k]=nums[i]
                k+=1
                i+=1

            elif(i>=m and j<n):
                nums1[k]=nums2[j]
                k+=1
                j+=1

            else:
                if(nums[i]<nums2[j]):
                    nums1[k]=nums[i]
                    k+=1
                    i+=1

                else:
                    nums1[k]=nums2[j]
                    k+=1
                    j+=1

       
        return
