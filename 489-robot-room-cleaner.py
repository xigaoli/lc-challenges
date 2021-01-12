# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
#example Input:
# room = [
#   [1,1,1,1,1,0,1,1],
#   [1,1,1,1,1,0,1,1],
#   [1,0,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0,0],
#   [1,1,1,1,1,1,1,1]
# ],
# row = 1,
# col = 3
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        #backtracking
        visited=set()
        #four directions,  up->right->down->left
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        def goback():
            #turn 180, go, turn 180 again
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            return
        #current direction is important, it decides what is next direction
        def backtrack(i,j,curr_d):
            visited.add((i,j))  #its fine if visit again
            robot.clean()   #its fine if clean again
            # print("clean [{},{}]".format(i,j))
            nextd=curr_d
            for _ in range(4):
                
                i1=i+directions[nextd][0]
                j1=j+directions[nextd][1]
                
                if((i1,j1) not in visited):
                    rslt = robot.move()
                    if(rslt == True):
                        # print("move into {},{}".format(i1,j1))
                        backtrack(i1,j1,nextd)
                        goback()    #important: goback!
                    #else: #obstacle - cannot move
                        
                # else:
                    #visited, should not move
                    # print("cannot move into {},{} - visited".format(i1,j1))
                #now turn right, go next
                # print("turn right at {},{}".format(i,j))
                robot.turnRight()
                nextd=(nextd+1)%4
            #finished tracking for this cell
            return
        backtrack(1,3,0)
