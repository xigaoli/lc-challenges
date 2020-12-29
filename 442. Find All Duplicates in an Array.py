class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #1<=num<=len(nums)
        output=[]
        for i in range(len(nums)):
            n=abs(nums[i])
            v=nums[abs(n)-1]
            if(v>0):
                nums[n-1]=-v
            else:
                output.append(n)
        return output
        # output=[]
        # s = set()
        # for i in range(len(nums)):
        #     n=nums[i]
        #     if(n in s):
        #         output.append(n)
        #     else:
        #         s.add(n)
        # return output