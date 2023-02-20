
# coding: utf-8




from numpy import *
from matplotlib import pyplot as plt
import sys


def loadDataSet(fileName = 'iris_with_cluster.csv'):
    dataMat=[]
    labelMat=[]
    fr = open(fileName)
    for line in fr.readlines():
        lineArray=line.strip().split(',')
        records = []
        for attr in lineArray[:-1]:
            records.append(float(attr))
        dataMat.append(records)
        labelMat.append(int(lineArray[-1]))
    dataMat = array(dataMat)
    
    labelMat = array(labelMat)
    
    
    return dataMat,labelMat

def pca(dataMat, PC_num=2):
    '''
    Input:
        dataMat: obtained from the loadDataSet function, each row represents an observation
                 and each column represents an attribute
        PC_num:  The number of desired dimensions after applyting PCA. In this project keep it to 2.
    Output:
        lowDDataMat: the 2-d data after PCA transformation
    '''
    rm = dataMat - mean(dataMat, axis = 0)

    va, ve = linalg.eig(mat(cov(rm, rowvar = 0)))

    ve = ve[:, argsort(va)[::-1]]
    ve = ve[:, :PC_num]

    return array(rm * ve)


def plot(lowDDataMat, labelMat, figname):
    '''
    Input:
        lowDDataMat: the 2-d data after PCA transformation obtained from pca function
        labelMat: the corresponding label of each observation obtained from loadData
    '''
    fg = plt.figure()

    tmp = fg.add_subplot(111)

    cl = ['purple', 'green', 'yellow']
    for i in range(len(cl)):
        x = lowDDataMat[labelMat == i + 1][:, 0]
        y = lowDDataMat[labelMat == i + 1][:, 1]

        tmp.scatter(x, y, c=cl[i], label='Cluster %d' % (i + 1))

    tmp.legend()
    tmp.set_xlabel('PC1')
    tmp.set_ylabel('PC2')
    tmp.set_title('PCA of %s' % figname)

    plt.savefig(figname)
    


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'iris_with_cluster.csv'
    figname = filename
    figname = figname.replace('csv','jpg')
    dataMat, labelMat = loadDataSet(filename)
    
    lowDDataMat = pca(dataMat)
    
    plot(lowDDataMat, labelMat, figname)
    

