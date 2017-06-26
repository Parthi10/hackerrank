class PetrolPump(object):
    def __init__(self, petrol, distance):
        self.petrol = petrol
        self.distance = distance
        self.nextPP = None

class CyclicLinkedList(object):
    def __init__(self):
        self.list = []

    def add(self, petrol, distance):
        newPP = PetrolPump(petrol, distance)
        if self.list:
            lastPP = self.list[-1]
            lastPP.nextPP = newPP
        self.list.append(newPP)

    def cyclise(self):
        lastPP = self.list[-1]
        firstPP = self.list[0]
        lastPP.nextPP = firstPP

n = int(input().strip())
C = CyclicLinkedList()

for i in range(n):
    p, d = map(int, input().strip().split(' '))
    C.add(p, d)

C.cyclise()

i = 0
while i<n:
    PP = C.list[i]
    petrol, distanceToCover = PP.petrol, PP.distance
    nxPP = PP.nextPP
    completed = False
    x = i
    while distanceToCover<=petrol:
        petrol -= distanceToCover
        if nxPP == PP:
            completed = True
            break
        petrol += nxPP.petrol
        distanceToCover = nxPP.distance
        nxPP = nxPP.nextPP
        x += 1
    if not completed:#if start at any PPs b/w i to x+1 we wouldn't complete the circle
        i = x+1
    if completed:
        break

print(i)
