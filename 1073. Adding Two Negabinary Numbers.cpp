class Solution {
public:
    vector<int> addNegabinary(vector<int>& arr1, vector<int>& arr2) {
        //use 2 carrys
        //special case: carry2=1, carry1=2, then canceled to 0
        // rslt = d1+d2+carry1={0,1,2,3,4}
        // (0,1): no need to update carry
        // (2): dr=0, carry1+=1,carry2+=1 -> 2*(-2)^(i)=(-2)^(i+2)+(-2)^(i+1) (110)
        // (3): dr=1, carry1+=1,carry2+=1 -> 3*(-2)^(i)=(-2)^(i+2)+(-2)^(i+1)+(-2)^i (111)
        // (4): dr=0, carry2+=1           -> 4*(-2)^(i)=(-2)^(i+2)
        // dr=rslt%2
        int carry1=0;
        int carry2=0;
        
        int i=arr1.size()-1;
        int j=arr2.size()-1;
        
        vector<int> ans;
        //calc shared digits
        while(i>=0 || j>=0 || carry1>0 || carry2>0){
            int d1=0;
            
            if(i>=0){
                d1=arr1[i];
                i--;
            }
            int d2=0;
            
            if(j>=0){
                d2=arr2[j];
                j--;
            }
            int dr=0;//digit result
            int rslt=d1+d2+carry1;//add previous carry1 into current result
            //results are out, move to next -> carry2 is now new carry1, new carry2=0
            carry1=carry2;
            carry2=0;
            dr=rslt%2;      //digit is always rslt%2
            //0 or 1 no need to update carry
            if(rslt==2 || rslt == 3){
                //carry1+=1,carry2+=1
                carry1+=1;
                carry2+=1;
            }
            else if(rslt==4){
                carry2+=1;
            }
            if(carry2==1 && carry1==2){
                //special case
                carry2=0;carry1=0;
            }
            ans.push_back(dr);
        }
        //ans is reversed, remove leading zeroes first
        while(ans.size()>1 && ans.back()==0){
            ans.pop_back();
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};