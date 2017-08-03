#include <iostream>

using namespace std;

int main(){
    int t,n,i,j,k;
    cin>>t;
    for(i=0;i<t;i++){
        cin>>n;
        int arr[n];
        for(j=0;j<n;j++){
            cin>>arr[j];
        }

        int dp[n]={0};
        int max =0;
        for(j=0;j<n;j++){
            dp[j]=arr[j];//j=0,1
            if (j>=2){
                if(dp[j-1]-arr[j-1]>dp[j-2]){
                    dp[j]=dp[j-3]+arr[j];
                }
                else{
                    dp[j]=dp[j-2]+arr[j];
                }
            }
            if (dp[j]>max) max=dp[j];
        }
        cout<<max<<endl;

    }
    return 0;
}
