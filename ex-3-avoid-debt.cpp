#include <iostream>
#include <vector>
#include <queue>
using namespace std;

//a list of expected revenues and payments
// can move expense(negative number) to the end of arr
//scan from begin to end, calc sum
//try avoid debt(negative sum)

//use priority queue to record seen negative num
//when meet a negative, move most negative num to the end of arr

int solution(vector<int> &A){
	int n=A.size();
	int vsum=0;
	int pop_cnt=0;
	priority_queue<int,vector<int>,greater<int>> pq;
	for(int i=0;i<n;i++){
		pq.push(A[i]);
		vsum+=A[i];
		//cout<<"vsum="<<vsum<<endl;
		if(vsum<0){
			//meet debt
			//deque one from priority queue
			if(pq.size()<=0){
				//no solution
				return -1;
			}
			int mostNeg = pq.top();
			A.push_back(mostNeg);
			vsum-=mostNeg;
			pq.pop();
			pop_cnt++;
			cout<<"popped"<<mostNeg<<",vsum="<<vsum<<endl;
		}
	}
	return pop_cnt;
}

int main() {
	// your code goes here
	vector<int> A={-1,-1,-1,1,1,1,1};
	int rslt = solution(A);
	cout<<"rslt="<<rslt<<endl;
	return 0;
}