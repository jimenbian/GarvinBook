import math
import operator


def euclideanDistance(inst1, inst2, length):
    distance = 0
    for x in range(length):
        distance += pow((inst1[x] - inst2[x]), 2)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
            
        else:
            classVotes[response] = 1
            
    sortedVotes = sorted(classVotes.iteritems(), key = operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]