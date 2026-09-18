class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2: return len(stones)
            
        heapq._heapify_max(stones)

        while stones:
            x = heapq.heappop_max(stones)
            try:
                y = heapq.heappop_max(stones)
                if x < y: heapq.heappush_max(stones, y-x)
                elif x > y: heapq.heappush_max(stones, x-y)
            except: return x
                
        return 0