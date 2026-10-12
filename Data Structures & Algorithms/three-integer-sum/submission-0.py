class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        mem = dict({(v,k) for (k,v) in enumerate(nums)})
        result = []
        # visited = [[0 for i in range(len(nums))] for j in range(len(nums))]
        visited = {}

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    target = nums[i] + nums[j]
                    if -target in mem:
                        idx = mem[-target]
                        if idx != i and idx != j:
                            result_set = ",".join([str(i) for i in list(sorted([nums[mem[-target]], nums[i], nums[j]]))])
                            print(result_set)
                            if result_set not in visited:
                                result.append([nums[mem[-target]], nums[i], nums[j]])
                                visited[result_set] = 1
        return result





        