#Artificial Neural Network

import random
import copy
import matplotlib.pyplot as plt
from math import *

"""==================Matrix Actions======================="""

#Create Matrix
def MatrixCreate(row,column):
    return [[0 for i in range(column)] for j in range(row)]

#Randomize Matrix
# mode :: 0(default) = [0,1] || 1 = {0,1}
# section randomized = 1 line
def MatrixRandomize(v,mode=0,sec = 0):
    
    for row in range(len(v)):
        for column in range(len(v[0])):
            
            if mode == 0:
                v[row][column] = random.random()
            if mode == 1:
                v[row][column] = random.randint(0,1)
                
        if sec != 0:
            break

    return v

#Perturb Matrix
# mode:: default(0) = random() || 1 == randint()
def MatrixPerturb(v,prob,mode = 0):
    c = copy.deepcopy(v)
    
    for row in range(len(c)):
        for column in range(len(c[0])):
    
            if random.random() < prob:
                if mode == 0:
                    c[row][column] = random.random()
                if mode == 1:
                    c[row][column] = random.randint(0,1)
                
    return c


#Fitness
def Fitness(v):
    n = float(len(v)*len(v[0]))
    s = 0

    for row in range(len(v)):
        for column in range(len(v[0])):
            s += v[row][column]/n
    return s
    

#Print Matrix
def MPrint(v):
    for row in v:
        print row
    return

"""=================Hill Climber===================="""

#Plot Graph
def VectorAsLine(fits):
    for species in fits:
        plt.plot(species)


"""=================Neural Network============"""

#Neuron Position Plotter
def NeuronPosition(NV):
    totalNeurons = len(NV[0])
    M = MatrixCreate(2,totalNeurons)
    
    for neuralPoint in range(totalNeurons):
        x = cos(2*pi/totalNeurons*neuralPoint)
        y = sin(2*pi/totalNeurons*neuralPoint)

        M[0][neuralPoint] = x
        M[1][neuralPoint] = y

    return M

def SynapticConnections(NP):
    for strt in range(len(NP[0])-1):
        for stp in range(strt+1,len(NP[0])):
            plt.plot([NP[0][strt],NP[0][stp]],[NP[1][strt],NP[1][stp]])    

def CircularPoint(NP):
    plt.plot(NP[0],NP[1], 'ko', markerfacecolor = [1,1,1], markersize = 18 )
            
"""=============Main====================="""

NeuronValues = MatrixRandomize(MatrixCreate(50,10),0,1)
NP = NeuronPosition(NeuronValues)

CircularPoint(NP)
SynapticConnections(NP)
plt.show()


























































        
