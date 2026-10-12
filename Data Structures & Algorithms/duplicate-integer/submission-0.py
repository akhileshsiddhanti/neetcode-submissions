class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mem = set()
        for i in nums:
            if i in mem:
                return True
            else:
                mem.add(i)
        return False