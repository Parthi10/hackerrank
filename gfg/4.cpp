//http://practice.geeksforgeeks.org/problems/index-of-first-1-in-a-sorted-array-of-0s-and-1s/0
#include <iostream>
#include <string>
using namespace std;

int main(){

  int t, n, i=0, j, k, v, index;
  cin>>t;
  string farji;
  for(k=0;k<t;k++){
    cin>>n;
    index=0;
    for(j=0;j<n;j++){
      cin>>v;
      if (v==1){
        cout<<index<<endl;
        getline(cin, farji);
        break;
      }
      index++;
    }
    if(index==n) cout<<-1<<endl;
  }
}
