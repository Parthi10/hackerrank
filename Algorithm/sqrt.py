import math
inputOK=True
while inputOK:
    base=float(input('enter base:'))
    if type(base) == type(1.0): inputOK= False
    else: print('error bro!!') 
inputOK=True
while inputOK:
    height=float(input('enter height:'))
    if type(height) == type(1.0): inputOK= False
    else: print('error bro!!')
hyp=math.sqrt (base*base+height*height)
print('base:' +str(base)  +',height:' +str(height) + ',hyp:' +str(hyp))
