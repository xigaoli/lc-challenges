// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector< vector<int> > &A) {
    // write your code in C++14 (g++ 6.2.0)
    //find max in matrix as M
    //cross out M, find remaining max as K
    //find A=max1 and B=max2 in col(M) and row(M), not including M
    // either choose M+K or A+B.
    int n=A.size();
    int m=A[0].size();
    //min element is 0
    int M1=-1;
    int Mrow=-1;//row of M
    int Mcol=-1;//col of M
    // cout<<m<<endl;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            //data=A[i][j]
            if(A[i][j]>M1){
                M1=A[i][j];
                Mrow=i;
                Mcol=j;
            }
        }
    }
    // cout<<"M1="<<M1<<",mrow="<<Mrow<<",mcol="<<Mcol<<endl;
    int K=-1;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(i==Mrow || j==Mcol) continue;//skip rowM and colM
            if(A[i][j]>K){
                K=A[i][j];
                // krow=i; //for debug only, not necessary
                // kcol=j;
            }
            
        }
    }
    // cout<<"K="<<K<<endl;
    int A1=-1;
    int B1=-1;
    //A1=A[i][mcol]
    //B1=A[mrow][j]
    for(int i=0;i<n;i++){
        if(i==Mrow) continue;
        if(A[i][Mcol]>A1){
            A1=A[i][Mcol];
        }
    }
    // cout<<"A1="<<A1<<endl;
    for(int j=0;j<m;j++){
        if(j==Mcol) continue;
        if(A[Mrow][j]>B1){
            B1=A[Mrow][j];
        }
    }
    // cout<<"B1="<<B1<<endl;
    int ans = std::max((M1+K),(A1+B1));
    return ans;
}