#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q, i, j, z, k, temp;
    cin>>n>>q;
    vector <vector<int>> a;
    for(i=0; i<n; i++){
        cin>>k;
        vector <int> a_i;
        for(j=0; j<k; j++){
            cin>>temp;
            a_i.push_back(temp);
        }
        a.push_back(a_i);
    }
    for(z=0; z<q; z++){
        cin>>i>>j;
        cout<<a[i][j]<<endl;
    }
    return 0;
}
