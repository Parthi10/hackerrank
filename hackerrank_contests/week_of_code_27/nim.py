
#!/bin/python3

import sys
def nim(heaps, misere=False):
    if heaps==[0,1]: return (1,1)
    X = reduce(lambda x,y: x^y, heaps)#gives the xor of all the elements of the list
    if X == 0: # Will lose unless all non-empty heaps have size one
        # if max(heaps) > 1:
        #     print "You will lose :("
        for i, heap in enumerate(heaps):
            if heap > 0: # Empty any (non-empty) heap
                chosen_heap, nb_remove = i, heap
                break
    else:
        sums = [t^X < t for t in heaps]
        chosen_heap = sums.index(True)
        nb_remove = heaps[chosen_heap] - (heaps[chosen_heap]^X)
        heaps_twomore = 0
        for i, heap in enumerate(heaps):
            n = heap-nb_remove if chosen_heap == i else heap
            if n>1: heaps_twomore += 1
        if heaps_twomore == 0:
            chosen_heap = heaps.index(max(heaps))
            heaps_one = sum(t==1 for t in heaps)
            nb_remove = heaps[chosen_heap]-1 if heaps_one%2!=misere else heaps[chosen_heap]
    return chosen_heap, nb_remove



g = int(raw_input().strip())
for a0 in range(g):
    n = int(raw_input().strip())
    heaps = [int(p_temp) for p_temp in raw_input().strip().split(' ')]
    # print(heaps)
    step_count=0
    if n == heaps.count(1):
        if n%2 == 0:
            print("L")
        else:
            print("W")
    else:
        while not all(i==0 for i in heaps):
            nim_sum = reduce(lambda x,y: x^y, heaps)
            if nim_sum==0:
                zero_moves = len(heaps) - heaps.count(0)
                if zero_moves%2 != 0:
                    step_count += 1
                    break
            move = nim(heaps,misere=False)
            # print("Move", move)
            heaps[move[0]] -= move[1]
            step_count += 1
        if step_count%2 == 0:
            print("L")
        else:
            print("W")
