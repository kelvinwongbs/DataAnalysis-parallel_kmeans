import sys
import os
import numpy as np

dim = 20

# read centroids.txt file
centroids = np.zeros((10, dim))
with open('centroids.txt', 'r') as file:
    for line in file:
        cid, c_image = line.strip().split('\t')
        c_pixels = c_image.split()
        centroids[int(cid)] = [float(pixel) for pixel in c_pixels]

# variables emit at the end of mappper
c_partialSum = np.zeros((10, dim))
c_partialCount = np.zeros(10)

# mapper
for line in sys.stdin:
    # key-value pair
    id, image = line.strip().split('\t', 1)
    # split value to array of pixels
    pixels = image.split()
    # convert to float
    pt = np.zeros((dim))
    pt = [float(pixel) for pixel in pixels]

    # calculate distances
    d = np.zeros(10)
    for i in range(10):
        # euclidean distance
        d[i] = np.sqrt(np.sum(np.square(centroids[i] - pt)))
    # assign to nearest centroid
    assign_cid = np.argmin(d)

    # add this data point to partial sum of its assigned centroid
    c_partialSum[assign_cid]  += pt
    # add 1 to no. of data points of the assigned centroid
    c_partialCount[assign_cid] += 1

# cleanup
for i in range(10):
    # convert partial sum to string
    s = ""
    for e in c_partialSum[i]:
        s = s + str(e) + " "
    s = s.strip() + ":" + str(c_partialCount[i])
    # centroid id, partial sum : count
    print('%s\t%s' % (i, s))