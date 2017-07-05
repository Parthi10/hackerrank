#include <stdio.h>
#include <iostream>
using namespace std;
void update(int *a,int *b) {
    int temp1, temp2;
    temp1 = *a + *b;
    temp2 = abs(*a -*b);
    *a = temp1;
    *b = temp2;
}

int main() {
    int a, b;
    cin>>a;
    cin>>b;
    int * pa = &a;
    int * pb = &b;
    update(pa, pb);
    cout<<a<<"\n"<<b<<endl;
}

