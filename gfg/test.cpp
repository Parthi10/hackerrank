#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <typeinfo>


using namespace std;

struct Node
{
    int data;
    Node* left, * right;
};

int main(){

    vector <int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);

    vector <int> :: iterator x;
    vector <int> :: iterator y;

    x = v.begin();
    y = v.begin()+1;

    cout<<&x<<endl;
    cout<<&y<<endl;

    // printf()
    cout<<*x<<endl;





    // Node * node = new Node();
    // node->data=12;
    // levelOrder(node);
    // return 0;






    /*
  string farji;
  int i;
  cin>>i;
  getline(cin, farji);
  cout<<i<<endl;
  cout<<farji<<endl;
*/

/*
  int j;
  vector <int> odd;

  int a[5] = {1,2,3,4,5};
  for(j=0; j<5; j++){
      odd.insert(odd.begin(), a[j]);
  }

  for(j=0; j<5; j++){
    cout<<odd.at(j)<<" ";
  }
  cout<<endl;
  for(j=0;j<5;j++){
    cout<<odd.back()<<" ";
    odd.pop_back();
  }
  cout<<endl;
*/
  // return 0;

}

void levelOrder(Node* node)
{
    vector <Node *> v;
    cout<<v.capacity()<<endl;
    cout<<v.size()<<endl;

    cout<<sizeof(node)<<endl;
    v.insert(v.begin(), node);
    cout<<"asdf"<<endl;
    cout<<v.capacity()<<endl;
    cout<<v.size()<<endl;
    while(!v.empty()){
        //vector <Node *> :: iterator itr = v.end();
        node = v.front();
        v.pop_back();
        // cout<<*(*v.end())<<" ";
        // cout<<typeid(n).name()<<endl;
        cout<<node->data<<endl;
        break;
        /*
        if(node->left!=NULL){
            v.insert(v.begin(), node->left);
        }
        if(node->right!=NULL){
            v.insert(v.begin(), node->right);
        }
        */

    }
}
