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
            if mode == -1:
                v[row][column] = random.uniform(1,-1)
                
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

def SynapticConnections(NP,syn):
    for strt in range(len(NP[0])-1):
        for stp in range(strt+1,len(NP[0])):

            #Synaptic Width
            lineWidth = int(10*abs(syn[strt][stp]))+1

            #Line Colour
            if syn[strt][stp]<0:
                lineColor = [0.8,0.8,0.8]
            if syn[strt][stp]>=0:
                lineColor = [0.0,0.0,0.0]
                
            plt.plot([NP[0][strt],NP[0][stp]],[NP[1][strt],NP[1][stp]],color = lineColor, linewidth = lineWidth, alpha=0.5)    
    
def CircularPoint(NP):
    plt.plot(NP[0],NP[1], 'ko', markerfacecolor = [1,1,1], markersize = 18 )

def Update(NV, Syn, i):
    for n in range(len(NV[0])):
        for strenght in range(len(NV[0])):            
            NV[i][n] += Syn[n][strenght]*NV[i-1][strenght]
                
        if NV[i][n]<0:
            NV[i][n] = 0
        if NV[i][n] > 1:
            NV[i][n] = 1
            
    return NV
    
"""=============Main====================="""

NeuronValues = MatrixRandomize(MatrixCreate(50,10),0,1)
NP = NeuronPosition(NeuronValues)

Synapses = MatrixRandomize(MatrixCreate(10,10),-1)
#CircularPoint(NP)
#SynapticConnections(NP, Synapses)
#plt.show()

for i in range(1,50):    
    NeuronValues = Update(NeuronValues, Synapses, i)

    
plt.imshow(NeuronValues, cmap=plt.cm.gray, interpolation = "nearest", aspect="auto")
plt.show()
    

























































        
