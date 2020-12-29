class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #greedy:
        def pickSecond(item):
            return item[1]
        if(len(points)==0):
            return 0
        currentArrowEnd=float('-inf')
        points.sort(key=pickSecond)
        arrowCount=0
        
        for pt in points:
            if(pt[0]>currentArrowEnd):
                arrowCount+=1
                currentArrowEnd=pt[1]
        return arrowCount
            