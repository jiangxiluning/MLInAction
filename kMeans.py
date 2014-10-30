from numpy import *
import matplotlib 
import pylab
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine)
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA-vecB, 2)))

def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = minJ + rangeJ*random.rand(k,1)
    return centroids

def kMeans(dataSet,k , distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssmet = mat(zeros((m,2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssmet[i,0] != minIndex: clusterChanged = True
            clusterAssmet[i,:] = minIndex, minDist**2
        print centroids
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssmet[:,0].A == cent)[0]]
            centroids[cent,:] = mean(ptsInClust, axis=0)
    return centroids, clusterAssmet


def getScatter(dataSet, centroids, clustAssesing):
    pylab.close()
    colorSeq=([('r','b','g','y')[int(i[0])] for i in clustAssesing.A])
    pylab.scatter(dataSet[:,0],dataSet[:,1],c=colorSeq)
    pylab.scatter(centroids[:,0],centroids[:,1],marker='+',s=100)
    
    pylab.savefig('kmeans.png')
                