class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        #greedy
        #sort array by start
        #stitchPt=0,endPt=0,clipNum=0
        #compare, 4 cases
        #0. [stitchPt,endPt],[newclip0,newclip1] ->fail, ret -1
        #2. [stitchPt,{newclip0, endPt], newclip1] -> insert new clip update stitchpt to newclip0, clipNum++
        #3. {newclip0, [stitchPt, endPt], newclip1] -> replace previous clip, stitchPt no change, endPt=newClip1
        #1. [stitchPt,{newclip0,newclip1},endPt] -> discard, do nothing
        if(T==0):
            return 0
        clips.sort()
        if(clips[0][0]>0):
            return -1
        stitchPt=clips[0][0]
        endPt=clips[0][1]
        clipNum=1
        for newclip in clips:
            if(endPt<newclip[0]):
                #fail
                return -1
            elif(endPt<newclip[1]):
                if(stitchPt>=newclip[0]):
                    #case 3, replace
                    endPt=newclip[1]
                else:
                    #case 2, insert
                    clipNum+=1
                    stitchPt=endPt
                    endPt=newclip[1]
            if(endPt>=T):
                return clipNum
        #finished, but not reaching T, fail
        return -1
                    