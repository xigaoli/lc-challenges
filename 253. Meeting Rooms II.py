class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #sort
        intervals.sort()
        rslt=1  #at least 1 needed
        room=[]
        room.append(intervals[0][1])
        for i in range(1,len(intervals)):
            
            #[1,3],[2,5],[2,7] ->3
            #[1,3],[2,5],[2,7],#new[4,9] pop out all end <begin and push new
            #pop out
            curr_end=intervals[i][1]
            curr_begin=intervals[i][0]
            while(room and room[0]<=curr_begin):# pop all end <begin
                heapq.heappop(room)
            #room.append(curr)
            heapq.heappush(room,curr_end)
            #print(room)
            rslt = max(rslt,len(room))
        return rslt