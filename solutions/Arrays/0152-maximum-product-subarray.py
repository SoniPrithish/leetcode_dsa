class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product=nums[0]
        min_product=nums[0]
        result=nums[0]
        n=len(nums)
        for i in range(1,n):
            if nums[i]<0:
                max_product,min_product=min_product,max_product
            max_product=max(nums[i],nums[i]*max_product)
            min_product=min(nums[i],nums[i]*min_product)
            result=max(result,max_product)
        return result
