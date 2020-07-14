class Solution:
    def angleClock(self, h: int, m: int) -> float:
        if h == 12: 
            h = 0
        if m == 60: 
            m = 0
            h += 1; 
            if(h>12): 
                h = h-12
        hour = 0.5*(h*60 + m)
        minute = 6*m
        angle = abs(hour - minute)
        return min(angle, 360-angle)