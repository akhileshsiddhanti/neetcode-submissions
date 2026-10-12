class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums[::-1]
            
        prev_product = [0 for i in range(len(nums))]
        next_product = [0 for i in range(len(nums))]
        
        prev_product[0]  = 1
        next_product[-1] = 1

        for i in range(1, len(nums)):
            prev_product[i] = prev_product[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            next_product[i] = next_product[i+1] * nums[i+1]

        result = [prev_product[i] * next_product[i] for i in range(len(nums))]
        return result
        