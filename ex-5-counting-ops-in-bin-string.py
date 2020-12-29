# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#give a string S consists of 0 and 1
#OP1: if V is odd then subtract 1
#OP2: if V is even divide by 2
#when V == 0 end
#give how many ops needed for V to become 0

def solution(S):
    # write your code in Python 3.6
    # subtract 1 -> turn last digit from 1 to 0, does not shift
    # cond: v is Odd (last digit == 1)
    #
    # divide by 2-> right shift
    # cond: v is even (last digit ==0)
    # if meet 1, operations +2 (-1 then shift);
    # if meet 0, operations +1 (shift only)
    # only exception is for first "1" digit, which only need to -1, no shift
    # if S is "0000..0" return 0
    firstOneDigitPos=-1
    #find first non-zero (1) digit
    for i in range(len(S)):
        if(S[i]!="0"):
            firstOneDigitPos=i
            break
    
    if(firstOneDigitPos==-1):#no "1"s are found
        return 0
    ansOperations=0
    for i in range(firstOneDigitPos,len(S)):
        if(S[i]=="1"):
            ansOperations+=2
        else:
            ansOperations+=1
    #overcount the leading 1, compensate now
    ansOperations-=1
    return ansOperations