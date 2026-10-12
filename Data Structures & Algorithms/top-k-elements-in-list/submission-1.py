class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        h = []
        for key, value in freq.items():
            heapq.heappush_max(h, (value, key))

        return [p[1] for p in heapq.nlargest(k, h)]
        