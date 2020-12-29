class Solution {

public:
    string baseNeg2(int N) {
    /* if remainder ==0 then OK as base 2
    Imagine we have a negative base -2, N = -5, what happens then? Which one below do you think is the remainder formula?
    a) -5 = (-2) * 2 + (-1)
    b) -5 = (-2) * 3 + 1
    Guess what? The remainder should always be positive! That means the remainder is 1, not -1. The multiple should be 3, not 2.*/
        string ans;
        int r=-1;
        
        do{
            r = N%(-2);     //in C++, MOD follow a) situation, so the remainder can be -1 or 0
            //cout<<"r="<<r<<endl;
            if(r == -1){
                r=1;
            }
            N = (N-r)/(-2);
            //cout<<"n="<<N<<endl;
            
            //formula:
            // b//base = (k+1), b%base = （r-base)
            // b = base*(k+1) + (r-base)
            ans=((char)(r+'0'))+ans;
        }while(N!=0);
        return ans;
    }
};