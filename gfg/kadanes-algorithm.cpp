#include <iostream>

using namespace std;

void kadanes(int *arr, int n){
    int ans=0, sum=0, max=-100;
    bool flag=true;
    for(int j=0; j<n; j++){
        if(arr[j]>max) max=arr[j];

        if (sum+arr[j] > 0){
          sum+=arr[j];
          if(sum > ans) ans = sum;
          flag=false;
        }
        else{
            sum = 0;
        }
    }

    if (flag){
        cout<<max<<endl;
    }

    else{
        cout<<ans<<endl;
    }
}

int main(){
    int t, n ;
    cin>>t;
    for(int i=0; i<t; i++){
        cin>>n;
        int arr[n];
	for(int j=0; j<n; j++){
	    cin>>arr[j];
	}
        kadanes(arr, n);
    }
    return 0;
}
