class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        if n == 2:
            return min(heights[0], heights[1])

        prev_max_index = [0 for i in range(n)]
        next_max_index = [0 for i in range(n)]

        prev_max_index[0] = 0
        next_max_index[-1] = n-1

        for i in range(1,n):
            if heights[i-1] > heights[prev_max_index[i-1]]:
                prev_max_index[i] = i-1
            else:
                prev_max_index[i] = prev_max_index[i-1]

        for i in range(n-2,-1,-1):
            if heights[i+1] > heights[next_max_index[i+1]]:
                next_max_index[i] = i+1
            else:
                next_max_index[i] = next_max_index[i+1]

        max_water = 0
        print(heights)
        print(prev_max_index)
        print(next_max_index)

        for i in range(1,n-1):
            water = abs(prev_max_index[i] - next_max_index[i]) * min(
                heights[prev_max_index[i]], heights[next_max_index[i]])
            water_2 = min(heights[i], heights[i-1])
            max_water = max(max(water, max_water), water_2)
        
        return max_water
        
        