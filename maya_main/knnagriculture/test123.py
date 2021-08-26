import pandas as pd
df = pd.read_csv('data/dataset_feature.csv')
df1 = df.drop(df.columns[0], axis=1)
print('df',df1)
df2 = df1.iloc[:, :-1]
print('df2',df2)
df2.to_csv('edit12.csv', index = False)



import csv
import math
import operator


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += (pow((float(instance1[x]) - float(instance2[x])), 2))
    return math.sqrt(distance)


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1

    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
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
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


trainingSet = []
testSet = []
with open('edit12.csv', 'r') as csvfile:
    lines = csv.reader(csvfile)
    dataset = list(lines)
    # print(dataset)



    for x in range(len(dataset) - 1):
        for y in range(25):
            dataset[x][y] = float(dataset[x][y])
        trainingSet.append(dataset[x])

with open('test1.csv', 'r') as csvfile1:
    lines1 = csv.reader(csvfile1)
    # print(lines1)
    dataset1 = list(lines1)
    # print(dataset1)

    for p in range(len(dataset1)):
        for q in range(25):
            dataset[p][q] = float(dataset[p][q])
        testSet.append(dataset1[p])

print("trainingset:", trainingSet)
print("testingset:", testSet)
# print("1:",len(trainingSet))
# print("2:",len(testSet))
k = 1
predictions = []
for x in range(len(testSet)):
    neighbors = getNeighbors(trainingSet, testSet[x], k)
    response = getResponse(neighbors)
    print("\nNeighbors:", neighbors)
    print('\nResponse:', response)

    predictions.append(response)

accuracy = getAccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy) + '%')


import matplotlib.pyplot as plt

x = [0, 1, 2]
y = [accuracy, 0, 0]
plt.title('Accuracy')
plt.bar(x, y)
plt.show()