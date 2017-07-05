inputArray = [-1,2,4,0]
segmentTreeArraySize = (2 * len(inputArray)) - 1
minSegTreeArray = [float('inf')] * segmentTreeArraySize
maxSegTreeArray = [float('-inf')] * segmentTreeArraySize

def constructMinSegTreeArray(minSegTreeArray, inputArray, low, high, pos):
    if low == high:
        minSegTreeArray[pos] = inputArray[low]
        return
    mid = (low + high) // 2
    leftPos = (2 * pos) + 1
    rightPos = (2 * pos) + 2
    constructMinSegTreeArray(minSegTreeArray, inputArray, low, mid, leftPos)
    constructMinSegTreeArray(minSegTreeArray, inputArray, mid + 1, high, rightPos)
    minSegTreeArray[pos] = min(minSegTreeArray[leftPos], minSegTreeArray[rightPos])

def constructMaxSegTreeArray(maxSegTreeArray, inputArray, low, high, pos):
    if low == high:
        maxSegTreeArray[pos] = inputArray[low]
        return
    mid = (low + high) // 2
    leftPos = (2 * pos) + 1
    rightPos = (2 * pos) + 2
    constructMinSegTreeArray(maxSegTreeArray, inputArray, low, mid, leftPos)
    constructMinSegTreeArray(maxSegTreeArray, inputArray, mid + 1, high, rightPos)
    maxSegTreeArray[pos] = max(maxSegTreeArray[leftPos], maxSegTreeArray[rightPos])


#find min in inputArray[qlow : qhigh + 1]
def rangeMinQuery(minSegTreeArray, qlow, qhigh, low, high, pos=0):
    #total overlap
    if qlow <= low and qhigh >= high:
        return minSegTreeArray[pos]

    #no overlap
    else if qlow > high or qhigh < low:
        return float('inf')

    #partial overlap
    # if (qhigh > high and qlow <= high) or (qlow < low and qhigh >= low):
    else:
        leftPos = (2 * pos) + 1
        rightPos = (2 * pos) + 2
        mid = (low + high) // 2
        return min(rangeMinQuery(minSegTreeArray, qlow, qhigh, low, mid, leftPos),
                    rangeMinQuery(minSegTreeArray, qlow, qhigh, mid + 1, high, rightPos)
                )

def rangeMaxQuery(maxSegTreeArray, qlow, qhigh, low, high, pos=0):
    #total overlap
    if qlow <= low and qhigh >= high:
        return maxSegTreeArray[pos]

    #no overlap
    else if qlow > high or qhigh < low:
        return float('-inf')

    #partial overlap
    # if (qhigh > high and qlow <= high) or (qlow < low and qhigh >= low):
    else:
        leftPos = (2 * pos) + 1
        rightPos = (2 * pos) + 2
        mid = (low + high) // 2
        return max(rangeMaxQuery(maxSegTreeArray, qlow, qhigh, low, mid, leftPos),
                    rangeMaxQuery(maxSegTreeArray, qlow, qhigh, mid + 1, high, rightPos)
                )
