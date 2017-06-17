time=[str(i) for i in input().split(':')]
a=time[2]
s=a[0]+a[1]
zone=a[2]+a[3]
h,m=time[0],time[1]
#print(h,m,sec,zone)
#print(m)
if(zone=='AM' and int(h)!=00):
    print('%s:%s:%s' %(h,m,s))
# elif(h==12 and m==00 and s=00):
#     if(zone=='AM'):
#         print('00:00:00')
#     elif(zone=='PM')
#         print('12:00:00')
elif(zone=='PM' and int(h)!=12):
    h=int(h)+12
    print('%s:%s:%s' % (h, m, s))
elif(int(h)==00 and zone=='AM'):
    print('00:%s:%s' %(m,s))
elif(int(h)==00 and zone=='PM'):
    print('12:%s:%s'%(m,s))

