from itertools import combinations as combo

d = {'a':1,'b':2,'c':3,'d':4,'e':5}

def get_key_from_value(dic, value):
    return list(dic.keys())[list(dic.values()).index(value)]
ans = []
for i in combo(d.values(),2):
    print(i)
    x = i[0]
    y = i[1]
    if x + y == 5:
        ans.append([get_key_from_value(d,x) + get_key_from_value(d, y)])

print(ans)
