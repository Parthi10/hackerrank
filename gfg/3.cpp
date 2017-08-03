//http://practice.geeksforgeeks.org/problems/second-most-repeated-string-in-a-sequence/0
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main(){
    int t,n,i,j,k;
    string tmp;
    cin>>t;
    for(i=0;i<t;i++){
        cin>>n;
        vector <string> S;
        unordered_map<string, int> map;
        for(j=0;j<n;j++){
            cin>>tmp;
            if (map.find(tmp) != map.end()){
                map[tmp] += 1;
            }
            else{
                map[tmp] = 1;
            }
        }
        unordered_map<string, int> :: iterator itr;
        int max=0, second_max=0;
        string max_str,second_max_str;
        for(itr=map.begin(); itr!=map.end(); itr++){
            if (itr->second > max){
                second_max_str=max_str;
                second_max=max;
                max_str=itr->first;
                max=itr->second;
            }
            else if (itr->second>second_max){
                second_max=itr->second;
                second_max_str=itr->first;
            }
            // cout<<itr->first<<" : "<<itr->second<<endl;
        }
        cout<<second_max_str<<endl;
    }
    return 0;
}
