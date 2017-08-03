#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Node{
    public:
        int data;
        Node * left;
        Node * right;

        Node(int d){
            data=d;
        }
};

void levelOrder(Node node)
{
    queue <Node> v;
    v.push(node);
    while(!v.empty()){
        node = v.front();
        v.pop();
        cout<<node.data<<" ";
        if(node.left!=NULL){
            v.push(*node.left);
        }
        if(node.right!=NULL){
            v.push(*node.right);
        }
    }
}


int main(){
    Node node = Node(12);
    cout<<node.data<<endl;

    return 0;
}
