class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        b = defaultdict(int)
        lmax = 0
        for num in nums:
            if not b[num]:
                prev_l = b[num-1]
                next_l = b[num+1]
                l = b[num] = prev_l + next_l + 1
                b[num - prev_l] = l
                b[num + next_l] = l
                lmax = max(l, lmax)
        return lmax
            





        