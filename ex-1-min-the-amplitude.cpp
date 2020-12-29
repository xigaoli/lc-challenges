//problem:
//give array A, remove K consecutive numbers in array -> A', 
//what is the min of amplitude(i.e. max(A')-min(A') )?
//use prefixsum and suffixsum

#include <iostream>
#include <vector>
using namespace std;

int printarray(vector<int> &A){
	for(int i=0;i<A.size();i++){
		cout<<A[i]<<",";
	}
	cout<<endl;
	return 0;
}


int solution(vector<int> &A, int K){
	int n=A.size();
	vector<int> premax(n);//max value in A[0...i]
	vector<int> premin(n);//min value in A[0...i]
	vector<int> sufmax(n);//max value in A[i...n]
	vector<int> sufmin(n);//min value in A[j...n]
	premax[0]=A[0];
	premin[0]=A[0];
	sufmax[n-1]=A[n-1];
	sufmin[n-1]=A[n-1];
	for(int i=1;i<n;i++){
		
		premax[i]=max(premax[i-1],A[i]);
		premin[i]=min(premin[i-1],A[i]);
		//cout<<premin[i-1]<<" ";
	}
	
	
	for(int i=n-2;i>=0;i--){
		sufmax[i]=max(sufmax[i+1],A[i]);
		sufmin[i]=min(sufmin[i+1],A[i]);
		//cout<<sufmin[i+1]<<" ";
	}
	printarray(premax);
	printarray(premin);
	printarray(sufmax);
	printarray(sufmin);
	
	
	
	
	//remove K consecutive items
	//remove i+1,i+2,...i+k elements, become 2 array A1,A2
	//then max = max((max(A1),max(A2)), min=min(min(A1),min(A2))
	//amp = max-min
	int maxamp=-1;
	//two corner case:
	//[] and A2(A[k+1]...A[n])
	int amphead=sufmax[K]-sufmin[K];
	cout<<"amphead="<<amphead<<endl;
	//A1(A[0]...A[n-K-1]) and []
	int amptail=premax[n-K-1]-premin[n-K-1];
	cout<<"amptail="<<amptail<<endl;
	maxamp = min(amphead,amptail);
	
	for (int i=0;i+K+1<n;i++){
		int maxv=max(premax[i],sufmax[i+K+1]);//max(A1)
		int minv=min(premin[i],sufmin[i+K+1]);//max(A2)
		int curramp = maxv-minv;
		cout<<"amp["<<i+1<<".."<<i+K<<"]="<<curramp<<endl;
		maxamp=min(maxamp,curramp);
	}
	
	return maxamp;
}

int main() {
	// your code goes here
	vector<int> A={5,3,6,1,3};
	printarray(A);
	cout<<endl;
	int K=2;
	int rslt = solution(A,K);
	cout<<"rslt:"<<rslt<<endl;
	return 0;
}
//K from 1 to n-1
//test example:
//A=[5,3,6,1,3],K=2,return 2 - remove [6,1]
//A=[8,8,4,3],K=2,return 0 - remove last 2
//A=[3,5,1,3,9,8],K=4,return 1 - remove first 4


//A=[5,3,6,1,3],K=1,return 3 - remove [1]
//A=[1,2,3,4,5,6],K=4,return 1 - remove last 4
//A=[1,2,3,4,5,6],K=5,return 1 - remove last 5