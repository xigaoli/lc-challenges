class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        totaldist=0
        for i in range(1,len(points)):
            distx=abs(points[i-1][0]-points[i][0])
            disty=abs(points[i-1][1]-points[i][1])
            totaldist+=max(distx,disty)
        return totaldist
