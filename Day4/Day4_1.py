# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):

        intervals.sort(key=lambda x: x.start)
        res = []

        pos = intervals[0]

        for i in intervals:
            if i.start <= pos.end:
                if i.end > pos.end:
                    pos.end = i.end
            else:
                res.append(pos)
                pos = i

        res.append(pos)
        return res


