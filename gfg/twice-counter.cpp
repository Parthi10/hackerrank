//http://practice.geeksforgeeks.org/problems/twice-counter/0
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
        int count=0;
        for(itr=map.begin(); itr!=map.end(); itr++){
            if(itr->second==2){
                count+=1;
            }
        }
        cout<<count<<endl;
    }
    return 0;
}
