//http://practice.geeksforgeeks.org/problems/even-and-odd-elements-at-even-and-odd-positions/0
#include <iostream>
#include <vector>

using namespace std;

void printVector(vector <int> arr){
  while(!arr.empty()){
    cout<<arr.back()<<" ";
    arr.pop_back();
  }
}

int main(){

  int t, n, i, j, o=0, e=0;

  cin>>t;
  for(i=0; i<t; i++){
    cin>>n;
    int a[n];
    for(j=0; j<n; j++){
      cin>>a[j];
    }
    vector <int> odd;
    vector <int> even;
    o=0;e=0;
    for(j=0; j<n; j++){
      if(a[j] & 1){
        odd.insert(odd.begin(), a[j]);
      }
      else{
        even.insert(even.begin(), a[j]);
      }
    }
    for(j = 0; j < n; j++){
      if(j & 1 && !odd.empty()){
        cout<<odd.back()<<" ";
        odd.pop_back();
      }
      else if (!(j&1) && !even.empty()){
        cout<<even.back()<<" ";
        even.pop_back();
      }
      else{//any one vector got empty
        if(odd.empty()){
          cout<<even.back()<<" ";
          even.pop_back();
        }
        else{
          cout<<odd.back()<<" ";
          odd.pop_back();
        }
      }
    }
    cout<<endl;
    odd.clear();
    even.clear();
  }

  return 0;
}
