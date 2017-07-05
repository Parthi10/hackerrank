#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

void print(int n){
    switch(n){
        case 1:
            cout<<"one"<<endl;
            break;
        case 2:
            cout<<"two"<<endl;
            break;
        case 3:
            cout<<"three"<<endl;
            break;
        case 4:
            cout<<"four"<<endl;
            break;
        case 5:
            cout<<"five"<<endl;
            break;
        case 6:
            cout<<"six"<<endl;
            break;
        case 7:
            cout<<"seven"<<endl;
            break;
        case 8:
            cout<<"eight"<<endl;
            break;
        case 9:
            cout<<"nine"<<endl;
            break;
    }
    return;
}

int main(){
    int a, b;
    cin >> a;
    cin >> b;
    for(int i=a; i<=b; i++){
        if(1 <= i && i <=9){
            print(i);
        }
        else if(i>9){
            if(i%2==0){
                cout<<"even"<<endl;
            }
            else{
                cout<<"odd"<<endl;
            }
        }
    }

    return 0;
}

