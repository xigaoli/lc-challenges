class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #opt
        if(len(nums1)>0 and len(nums2)>0):
            midA=getmedian(nums1)
            midB=getmedian(nums2)
            if(midA==midB):
                return midA
        #bin search
        ABLen = (len(nums1)+len(nums2))
        midk = ABLen//2
        if(ABLen%2==0):
            m1=getKthElem(nums1,0,nums2,0,midk)
            m2=getKthElem(nums1,0,nums2,0,midk+1)
            return (m1+m2)/2
        else:
            return getKthElem(nums1,0,nums2,0,midk+1)

def getmedian(arr):
    L = len(arr)//2
    if(len(arr)%2==0):
        return (arr[L-1]+arr[L])/2
    else:
        return arr[L]
        
def getKthElem(A,start1,B,start2,k):
        if(start1>=len(A)):
            return B[start2+k-1]
        if(start2>=len(B)):
            return A[start1+k-1]
        if(k==1):
            return min(A[start1],B[start2])
        halfk=k//2-1
        posA=start1+halfk
        posB=start2+halfk
        if(len(A)-posA<=0):
            halfkA=1
            halfkB=0
        elif(len(B)-posB<=0):
            halfkA=0
            halfkB=1
        else:
            halfkA=A[posA]
            halfkB=B[posB]

        if(halfkA<halfkB):
            return getKthElem(A,posA+1,B,start2,k-k//2)
        else:
            return getKthElem(A,start1,B,posB+1, k-k//2)