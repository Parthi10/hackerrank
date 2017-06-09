#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int q;
    int primeSet3 = 303;
    int primeSet3_zero = 37;
    int primeSet4 = 280;
    int primeSet4_zero = 135;
    int primeSet5 = 218;
    int primeSet5_zero = 175;
    int p[] = {218,95,101,295,513};
    int modulo = pow(10,9) + 7;

    scanf("%d",&q);
    for(int a0 = 0; a0 < q; a0++){
        int n;
        scanf("%d",&n);
        if (n>=5){
          if((int)n/5 ==1){
            if(n==5) printf("%d\n",primeSet5 % modulo);
            else if (n>5) printf("%d\n",p[n%5] % modulo);
          }
          else if ((int)n/5 > 1){
            int repeat = (int) n/5;
            int extra = n % 5;
            int ans = primeSet5 * pow(primeSet5_zero, repeat);
            if (extra == 4) printf("%d\n", (ans*primeSet4_zero)%modulo);
            else if (extra == 3) printf("%d\n",(ans*primeSet3_zero) %modulo);
            else if (extra == 2) printf("%d\n",(ans*85) %modulo);
            else if (extra == 1) printf("%d\n",(ans*92) %modulo );
            else if (extra == 0) printf("%d\n",ans%modulo);
          }
        }
        else if (n==4) printf("%d\n",primeSet4%modulo);
        else if(n==3) printf("%d\n",primeSet3 %modulo);
    }
    return 0;
}
