import xlrd
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt



#builds a hash of the states to their average data
loc = ('Public Data.xlsx')
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

table_hash = {}
for num in range(1,sheet.nrows):
    point = []
    for col in range(5):
        point.append(sheet.cell_value(num, col))
    editPoint = [point[0]]
    editPoint.append(point[2])
    editPoint.append(point[3])
    editPoint.append(point[4])

    table_hash[point[1]] = editPoint

places = []
salaries = []
charity_rate = []
charity_amount = []
for key, value in table_hash.items():
    places.append(value[0])
    salaries.append(value[1])
    charity_rate.append(value[2])
    charity_amount.append(value[3])

X = np.array([places, salaries, charity_rate, charity_amount]).T

kmeans = KMeans(n_clusters=9, random_state=0).fit(X)


print(kmeans.predict([[1,100000,40,2000], [2,90000,20,1800]]))
print(kmeans.cluster_centers_)


def getLabels(dataSet, centroids):
    print("hello world")

def shouldStop(oldCentroids, centroids, iterations, max_iterations):
    if iterations > max_iterations:
        return True
    else:
        return oldCentroids == centroids

def getRandomCentroids(numFeatures, k):
    centroidList = []
    for i in range(k):
        centroid = []
        centroid.append(np.random.randint(1,6))
        centroid.append(np.random.randint(1000,6000))
        centroid.append(np.random.uniform(low=0, high = 1))
        centroid.append(np.random.randint(1000,1400))
        centroidList.append(centroid)
    return centroidList

k = 6

numFeatures = len(X)
centroids = getRandomCentroids(numFeatures, k)

iterations = 0
oldCentroids = None

while not shouldStop(oldCentroids, centroids, iterations, 100):
    oldCentroids = centroids
    iterations += 1

