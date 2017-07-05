#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
long long int maxi(long long int a,long long int b)
{
    if(a>=b)
        return a;
    else
        return b;
}
long long int find_max(long long int fsum,long long int isum,long long int i,long long int j,long long int s1[],long long int s2[],long long int k,long long int m,long long int n)
{
    if (fsum>k)
        return 0;
    else
    {
       if(fsum-s1[i]==isum&&i>=n)
           return 0;
       else if(fsum-s2[j]==isum&&j>=m)
           return 0;

        return (1+maxi(find_max(fsum+s1[i],fsum,i+1,j,s1,s2,k,m,n),find_max(fsum+s2[j],fsum,i,j+1,s1,s2,k,m,n)));
    }
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int g=0;
    cin>>g;
    while(g--)
    {
        long long int n=0,m=0,x=0;
        cin>>n>>m>>x;
        long long int s1[n];
        long long int s2[m];
        for(long long int i=0;i<n;i++)
           cin>>s1[i];
        for(long long int i=0;i<m;i++)
            cin>>s2[i];
        long long int i=0,j=0;
        long long int c1=find_max(s1[i],0,i+1,j,s1,s2,x,m,n);
        long long int c2=find_max(s2[j],0,i,j+1,s1,s2,x,m,n);
        cout<<"ans="<<maxi(c1,c2)<<endl;

    }
    return 0;
}
