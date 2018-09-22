import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt


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


df = pd.DataFrame({
    "location": [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6],
    "salary": [1200,1000,1100, 2300,2400,2500, 3200,3245,3240, 4567,4512,4791, 4900,5000,5500, 6500,6000,6200],
    "donationChance": [.01,.012,.01, .02,.02,.02, .03,.03,.03, .046,.043,.04, .055,.051,.032, .06,.062,.058],
    "weightedDonationAmount": [1000,1200,1300, 1400,1200,1000, 1000,1200,1300, 1400,1200,1000, 1000,1200,1300, 1400,1200,1000]
})


k = 6

numFeatures = len(df)
centroids = getRandomCentroids(numFeatures, k)

iterations = 0
oldCentroids = None
