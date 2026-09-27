class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0; r = len(people)-1; boats = 0


        while l<r:

            # while r > -1 and people[r] == limit:
            #     boats += 1
            #     r -= 1
        
        
            calc = people[l] + people[r]
            

            if calc > limit:
                boats += 1
                r -= 1
                continue
            else:
                boats += 1
                r -= 1
            
            l += 1

        if l == r: boats += 1
            
            
            
        


        return boats
        