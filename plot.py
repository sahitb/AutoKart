import csv
import math
import matplotlib.pyplot as plt

data_array = []
time_stamp = -1
with open ('Data/1_EmptyHallway_ForwardBackward.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    next(csvReader)
    for row in csvReader:
        if row[0]!='-1':
            time_stamp=time_stamp+1
            data_array.append([])
        data_array[time_stamp].append(row)

# for i in 0:len(data_array)-1:
for i in range(0,10):
    x = []
    y = []
    for j in data_array[i]:
        angle_rad = float(j[1])*(2*math.pi/360)
        dist = float(j[2])
        x.append(dist*math.cos(angle_rad))
        y.append(dist*math.sin(angle_rad))
    plt.scatter(x,y)
