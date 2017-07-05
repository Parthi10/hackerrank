#include <iostream>
#include <vector>

using namespace std;

int max(int i, int j){
  if (i>j) return i;
  else return j;
}

int height(node * root){
  if (root == NULL){
    return -1;
  }
  else{
    return root -> ht;
  }
}

int setHeight(node * root){
  return (1 + max(height(root -> left), height(root -> right)));
}


int balance(node * root){
  return (height(root -> left) - height(root -> right));
}


node * rightRotate(node * root){
  node * LNode = root -> left;
  root -> left = LNode -> right;
  LNode -> right = root;
  root -> ht = setHeight(root);
  LNode -> ht = setHeight(LNode);
  return LNode;
}

node * leftRotate(node * root){
  node * RNode = root -> right;
  root -> right = RNode -> left;
  RNode -> left = root;
  root -> ht = setHeight(root);
  RNode -> ht = setHeight(RNode);
  return RNode;
}

node * insert(node * root, int val){
  if (root == NULL){
    node * root = new node;
    root -> val = val;
    root -> left = root -> right = NULL;
    root -> ht = 0;
    return root;
  }
  else if(val > root -> val){
    root -> right = insert(root -> right, val);
  }
  else{
    root -> left = insert(root -> left, val);
  }

  int bal = balance(root);
  if (bal > 1){
    if (balance(root->left) < 0){
      root -> left = leftRotate(root -> left);
    }
    root = rightRotate(root);
  }
  else if (bal < -1){
    if (balance(root->right) > 0){
      root -> right = rightRotate(root -> right);
    }
    root = leftRotate(root);
  }
  else{
    root -> ht = setHeight(root);
  }
  return root;
}
