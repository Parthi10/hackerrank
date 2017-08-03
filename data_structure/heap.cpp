#include <iostream>
#include <vector>
#include <unordered_map>
#include <limits>

using namespace std;

#define INT_MIN numeric_limits <int>::min()


class Node{
public:
    int data;
    Node(int d){data=d;}
    ~Node(){}
};


class Heap{
public:
    vector <Node *> v;
    unordered_map <Node *, int> map;//node to index in vector v

    void insert(Node * node){
        v.insert(v.end()-1, node);
        map[node] = v.size() - 1;
        BubbleUpFix(map[node]);
    }

    void deleteElement(Node * node){
        v[map[node]]->data = INT_MIN;
        BubbleUpFix(map[node]);
        extractMin();
    }

    Node * extractMin(){
        Node * node = v[0];
        v[0]->data = v[v.size()-1]->data;
        v.erase(v.end());
        heapify();
        return node;
    }

    void decrease(Node * node, int newvalue){
        v[map[node]]->data = newvalue;
        BubbleUpFix(map[node]);
    }

private:
    int getMinChildIndex(int parentIndex){
        int leftChild, rightChild;
        leftChild = 2*parentIndex;
        rightChild = 2*parentIndex+1;
        return (v[rightChild]->data < v[leftChild]->data) ? rightChild:leftChild;
    }

    void swap(int i, int j){
        int tmp = v[i]->data;
        v[i]->data = v[j]->data;
        v[j]->data=tmp;
    }

    void heapify(){
        int parentIndex=0, childIndex, tmp;
        childIndex=getMinChildIndex(parentIndex);
        while (v[parentIndex]->data>v[childIndex]->data){
            swap(parentIndex, childIndex);
            parentIndex=childIndex;
            childIndex=getMinChildIndex(parentIndex);
        }
    }

    void BubbleUpFix(int index){
        int parentIndex = index/2;
        while(v[parentIndex]->data > v[index]->data){
            swap(parentIndex, index);
            index /= 2;
            parentIndex /= 2;
        }
    }
};

int main(){

    return 0;
}
