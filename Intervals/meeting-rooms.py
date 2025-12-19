from typing import List

# Definition of Interval
class Interval(object):
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
    def __repr__(self):
        return f"Interval({self.start}, {self.end})"

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            if i1.end > i2.start:
                return False
        return True


# ---- Helpers & tests ----
def make_intervals(pairs: List[tuple]) -> List[Interval]:
    return [Interval(s, e) for s, e in pairs]

if __name__ == "__main__":
    s = Solution()

    # Overlapping -> False
    assert s.canAttendMeetings(make_intervals([(0, 30), (5, 10), (15, 20)])) is False

    # Non-overlapping -> True
    assert s.canAttendMeetings(make_intervals([(5, 8), (9, 15)])) is True

    # Touching at boundary (end == start) -> True
    assert s.canAttendMeetings(make_intervals([(0, 10), (10, 20)])) is True

    # Single or empty -> True
    assert s.canAttendMeetings(make_intervals([(1, 1)])) is True
    assert s.canAttendMeetings(make_intervals([])) is True

    print("All tests passed ✅")
