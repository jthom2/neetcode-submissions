"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) == 0:
            return True

        schedule = []


        intervals.sort(key=lambda x: x.start)
        
        j = 0
        for i in intervals:
            if j == 0:
                schedule.append((i.start, i.end))
            elif schedule[-1][1] > i.start:
                return False
            else:
                schedule.append((i.start, i.end))

            j += 1

             
        if len(schedule) == len(intervals):
            return True
        

        return False
