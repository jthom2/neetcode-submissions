class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [];  times = []; s = []; sp = True; same = set()

        if len(position) < 2: return len(position)
        for i in range(len(position)): ps.append([position[i], speed[i]])
        ps.sort(reverse=True)

        # print("[POS, MPH] — ",ps)

        for i in range(len(position)):
            t = (target - ps[i][0]) / (ps[i][1]) 
           
            
            s.append(t); same.add(ps[i][1])
            # print(i, s,end='  ')

            try:
                if s[-1] <= s[-2]: s.pop()
            except: pass
            # print(s)

        if len(same) == 1: return len(position)
        else: return len(s)