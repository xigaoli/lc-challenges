#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
//dice problem
//given 2 array of D6 - A1 and A2, how many reroll either in A1 or A2, can make sum(A1)==sum(A2)?

//greedy
//while true,
//get dmax from larger, get dmin from less (heap/priority queue)
//if(dmax==1 and dmin==6) return -1
//calc c1=(max-1), c2=(6-min)
//if(c1>c2) then roll c1 to 1, dec greater, else roll c2 to 6, inc less
//if(sumlarge<summin) return roll_cnt
//
int printarray(vector<int> &A){
	for(int i=0;i<A.size();i++){
		cout<<A[i];
		if(i+1!=A.size()) cout<<",";
	}
	cout<<endl;
	return 0;
}
int solution(vector<int> &A, vector<int> &B){
	int sumA=0,sumB=0;
	for(int i=0;i<A.size();i++){
		sumA+=A[i];
	}
	for(int i=0;i<B.size();i++){
		sumB+=B[i];
	}
	if(sumA==sumB){
		//special case
		return 0;
	}
	
	//assume A(maxheap) larger, B(minheap) less
	vector<int> maxheap,minheap;
	if(sumA<sumB){
		maxheap=B,minheap=A;
		int tmp=sumA;
		sumA=sumB;
		sumB=tmp;
	}
	else{
		maxheap=A,minheap=B;
	}
	printarray(maxheap);
	printarray(minheap);
	
	cout<<"sumA="<<sumA<<",sumB="<<sumB<<endl;
	
	//want A as max heap, B as min heap
	make_heap(maxheap.begin(),maxheap.end());//default is std::less<int>, ->max heap
	cout << "initial max heap A: " << maxheap.front() << endl;
	make_heap(minheap.begin(),minheap.end(),greater<int>());//min heap
	cout << "initial min heap B: " << minheap.front() << endl;
	int diff = sumA-sumB;
	int turncnt=0;
	int dice1,dice2;
	while(true){
		if(maxheap.size()>0){
			dice1=maxheap.front();
			
		}
		else{
			dice1=1;//nothing to turn
		}
		cout<<"dice1="<<dice1<<endl;
		if(minheap.size()>0){
			dice2=minheap.front();
			
		}
		else{
			dice2=6;//nothing to turn
		}
		cout<<"dice2="<<dice2<<endl;
		
		int v1=dice1-1;
		int v2=6-dice2;
		if(v1==0 and v2==0){
			//all turned over, no solution
			return -1;
		}
		int val=0;
		if(v1>=v2){
			//turn dice1 downward 1
			diff-=v1;
			pop_heap(maxheap.begin(),maxheap.end());maxheap.pop_back();
			cout<<"turn dice1,diff="<<diff<<endl;
		}
		else{
			//turn dice 2 upward 6
			diff-=v2;
			pop_heap(minheap.begin(),minheap.end(),greater<int>());minheap.pop_back();
			cout<<"turn dice2,diff="<<diff<<endl;
		}
		turncnt++;
		if(diff<=0){
			
			return turncnt;
		}
	}
	
	return 0;
}

int main() {
	// your code goes here
	vector<int> A={5,4,1,2,6,5};
	vector<int> B={2};
	int rslt = solution(A,B);
	cout<<"rslt="<<rslt<<endl;
	return 0;
}

//test case 1
// vector<int> A={5};
// vector<int> B={1,1,6}; ->return 1

// test case 2
// vector<int> A={2,3,1,1,2};
// vector<int> B={5,4,6}; ->return 6

// test case 3
// vector<int> A={5,4,1,2,6,5};
// vector<int> B={2}; ->return 6

// test case 4
//  vector<int> A={1,2,3,4,3,2,1};
//  vector<int> B={6}; ->return -1 - impossible
