#include <iostream>
#include <vector>

using namespace std;

int main(){

  int t, n, i, j, k, max;

  cin>>t;

  for(i=0;i<t;i++){

    cin>>n;
    int arr[n];
    int LIS[n];
    for(j=0;j<n;j++){
      cin>>arr[j];
    }
    for(j=0;j<n;j++){
      // cout<<"\nj = "<<j<<endl;
      max = 0;
      for(k=j-1;k>=0;k--){
        if(LIS[k] > max && arr[j] > arr[k]) max = LIS[k];
      }
      // cout<<"max = "<<max<<endl;
      LIS[j] = (max!=0) ? max + 1 : 1;
      // cout<<"LIS = "<<LIS[j]<<endl;
    }
    max=0;
    for(j=0;j<n;j++){
      if(max<LIS[j]) max=LIS[j];
    }
    cout<<max<<endl;
  }
  return 0;
}
