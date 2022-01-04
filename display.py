import numpy as np

c_images = [] # temp store of centroids data
# read centroids.txt file
centroids = np.zeros((10, 784))
with open('centroids.txt', 'r') as file:
    for line in file:
        cid, c_image = line.strip().split('\t')
        c_pixels = c_image.split()
        centroids[int(cid)] = [float(pixel) for pixel in c_pixels]
        c_images.append(c_image.strip())

count = np.zeros(10)
with open('train-images', 'r') as file:
    for line in file:
        # key-value pair
        pid, p_image = line.strip().split('\t', 1)
        # split value to array of pixels
        p_pixels = p_image.split()
        # convert to matrix of float
        pt = np.zeros((784))
        pt = [float(pixel) for pixel in p_pixels]

        # calculate distances
        d = np.zeros(10)
        for i in range(10):
            # euclidean distance
            d[i] = np.sqrt(np.sum(np.square(centroids[i] - pt)))
        # assign to nearest centroid
        assign_cid = np.argmin(d)
        count[assign_cid] += 1

for i in range(10):
    print('Centroid %d: [%s], %d' % (i, c_images[i], count[i]))
