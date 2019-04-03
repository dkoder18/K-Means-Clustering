import sys
import random
import math

df = sys.argv[1]

f = open(df)
data = []
l = f.readline ()

#################
### Read Data ###
#################

while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))

    data.append(l2)
    l = f.readline()

rows = len (data)
cols = len (data[0])

f.close()
######################
####### get k ########
######################

try:
    k = int(sys.argv[2])
except IndexError:
    print("INCORRECT PARAMETERS ENTERED:")
    print("Here, try - python hw8.py <trainlabels> <number of clusters>")
    sys.exit ()

##################################
########## initialize m ##########
##################################
m = []
col = []
for j in range (0, cols, 1):
    col.append (0)

for i in range (0, k, 1):
    m.append (col)

random1 = 0

for p in range (0, k, 1):
    random1 = random.randrange (0, (rows - 1))
    m[p] = data[random1]

#################################
##### classifying the points ####
#################################
trainlabels = {}
diff = 1

prev = [[0] * cols for x in range (k)]

dist = []

mdist = []
for p in range (0, k, 1):
    mdist.append (0)
n = []
for p in range (0, k, 1):
    dist.append (0.1)
for p in range (0, k, 1):
    n.append (0.1)
totaldist = 1
classes = []

while ((totaldist) > 0):
    for i in range (0, rows, 1):
        dist = []

        for p in range (0, k, 1):
            dist.append (0)
        for p in range (0, k, 1):
            for j in range (0, cols, 1):
                dist[p] += ((data[i][j] - m[p][j]) ** 2)
        for p in range (0, k, 1):
            dist[p] = (dist[p]) ** 0.5
        mindist = 0
        mindist = min (dist)

        for p in range (0, k, 1):
            if (dist[p] == mindist):
                trainlabels[i] = p
                n[p] += 1

    ##############################
    ###### compute means #########
    ##############################

    m = [[0] * cols for x in range (k)]
    col = []

    for i in range (0, rows, 1):
        for p in range (0, k, 1):

            if (trainlabels.get (i) == p):
                for j in range (0, cols, 1):
                    temp = m[p][j]
                    temp1 = data[i][j]
                    m[p][j] = temp + temp1

    for j in range (0, cols, 1):
        for i in range (0, k, 1):
            m[i][j] = m[i][j] / n[i]

    classes = [int (x) for x in n]
    n = [0.1] * k

    #############################################
    #### compute distance between means #########
    #############################################

    mdist = []
    for p in range (0, k, 1):
        mdist.append (0)
    for p in range (0, k, 1):
        for j in range (0, cols, 1):
            mdist[p] += float ((prev[p][j] - m[p][j]) ** 2)

        mdist[p] = (mdist[p]) ** 0.5

    prev = m
    totaldist = 0
    for b in range (0, len (mdist), 1):
        totaldist += mdist[b]

    print ("Distances between the means", totaldist)

print ("Number of datapoints in each of the", k, " clusters is", classes)

############################################
#### classification of unlabeled point  ####
############################################

for i in range (0, rows, 1):
    print (trainlabels[i], i)
