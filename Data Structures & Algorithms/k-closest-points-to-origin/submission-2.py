class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points): return points

        heap = []; heapq.heapify(heap); res = []
        
        for p in points:
            x = p[0]; y = p[1]
            heapq.heappush(heap, [math.sqrt(x*x + y*y), x, y])

        while len(res) != k:
            p = heapq.heappop(heap)
            res.append([p[1], p[2]])

        return res