n = int(input().strip())
for i in range(0,n):
    for y in range(0,n):
        if(y<n-i-1):
            print(' ', end='')
        elif(y>=n-i-1 and y!=n-1):
            print('#',end='')
        else:
            print('#')

