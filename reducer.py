import sys
from operator import itemgetter
from itertools import groupby
import numpy as np

dim = 20

# generator for data input
def read_mapper_output(input):
    for line in input:
        yield line.rstrip().split('\t', 1)


data = read_mapper_output(sys.stdin)
# reducer
#iterate keys
for key, key_value in groupby(data, itemgetter(0)):
    sum = np.zeros((dim))
    count = 0
    # iterate values
    for key, value in key_value:
        partialSum, partialCount = value.split(':')
        # add partial count to count
        count += float(partialCount)
        # array of float
        arr = [float(e) for e in partialSum.split()]
        # add partial sum (in array form) to sum
        sum += arr
    new_centroid = np.zeros((dim))
    new_centroid = sum / count
    s = ""
    for e in new_centroid:
        s = s + str(e) + " "
    print('%s\t%s' % (key, s))