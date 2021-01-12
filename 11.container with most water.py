class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxarea=0
        while(l<r):
            hl=height[l]
            hr=height[r]
            maxarea=max(maxarea, min(hl,hr)*(r-l))
            if(hl<hr):
                l+=1
            else:#> or =
                r-=1
        return maxarea