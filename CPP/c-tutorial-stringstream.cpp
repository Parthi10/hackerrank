#include <sstream>
#include <vector>
#include <iostream>

using namespace std;
vector <int> parseString(string str){
  vector <int> integers;
  stringstream ss(str);
  char comma;
  int i;
  while(ss>>i){
    integers.push_back(i);
    ss>>comma;
  }
  return integers;
}

int main(){
  string str;
  cin>>str;

  vector <int> integers;
  integers = parseString(str);
  for(int i=0; i< integers.size(); i++){
    cout<<integers[i]<<endl;

}
}
