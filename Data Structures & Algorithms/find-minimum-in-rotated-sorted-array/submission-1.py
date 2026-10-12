class Solution:
    def findMin(self, nums: List[int]) -> int:
        # n_0      n_mid      n_end
        print(nums)
        if len(nums) == 1:
            print("F")
            return nums[0]
        
        if len(nums) == 2:
            print("E")
            return min(nums[0], nums[1])

        if len(nums) <= 3:
            return min(nums)

        n = len(nums)

        n0 = nums[0]
        n_mid = nums[n//2]
        n_end = nums[-1]

        if n0 < n_mid:
            if n_mid < n_end:
                return self.findMin(nums[0:n//2 + 1])
            else:
                if n0 < n_end:
                    return self.findMin(nums[0:n//2 + 1])
                if n0 > n_end:
                    return self.findMin(nums[n//2:])



        if nums[0] < nums[n//2] and nums[n//2] < nums[-1]:
            print("D")
            return nums[0]
        
        if nums[0] < nums[n//2] and nums[n//2] > nums[-1]:
            if nums[0] > nums[-1]:
                print("C", nums[n//2:])    
                return self.findMin(nums[n//2:])

        if nums[0] > nums[n//2]:
            print("A", nums[0:n//2])
            return self.findMin(nums[0:n//2 + 1])
        else:
            print("B", nums[n//2:-1])
            return self.findMin(nums[n//2:])

        
        