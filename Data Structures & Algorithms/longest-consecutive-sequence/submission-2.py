class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        nums_min = min(nums)
        nums_max = max(nums)

        mem = [0 for i in range(nums_max-nums_min+1)]
        # print(nums)
        # print(mem)
        for i in range(len(nums)):
            mem[nums[i]-nums_min] = 1

        current = 0
        lcs = 0
        for i in range(len(mem)):
            if mem[i]:
                current += 1
                lcs = max(current, lcs)
            else:
                current = 0
        
        return lcs




        