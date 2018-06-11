import random
import copy
import matplotlib.pyplot as plt

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

#Plot Graph
def VectorAsLine(fits):
    for species in fits:
        plt.plot(species)

#main
fits = []

for cSpecies in range(1):  #iterations

    fits.append([])
    
    parent = MatrixRandomize(MatrixCreate(1,50))  #binary mode = 1
    pFitness = Fitness(parent) 

    for currentGen in range(2500):

        fits[cSpecies/25].append(pFitness)
        
        #print currentGen, pFitness
    
        child = MatrixPerturb(parent,0.05)  ## prob, mode ##binary mode = 1
        cFitness = Fitness(child)

        if cFitness > pFitness:
            parent = child
            pFitness = cFitness

VectorAsLine(fits)
plt.show()
















