class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_degree=360/60
        hour_degree=360/12
        
        
        min_angle=minutes*min_degree
        hour_angle = (hour%12+minutes/60)*hour_degree
        diff=abs(hour_angle-min_angle)
        return min(360-diff,diff)
        