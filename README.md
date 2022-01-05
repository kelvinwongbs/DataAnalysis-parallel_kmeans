# Implement parallel k-means clustering using Hadoop streaming (Python)

### Course: Web-scale Information Analytics

Dataset: MNIST handwritten digits (training set) from http://yann.lecun.com/exdb/mnist/  
Data are preprocessed in the following format:   
[id] \tab [784 integers seperated by space]

**Assume k = 10. Create a text file *centroids.txt* to store the 10 centroids.**

**Initialisation.py**   
Pick 10 random points from the dataset as centroids and save them in *centroids.txt*

**mapper.py**   
Input:   
All the points from the dataset

For each point, assign it to the nearest centroid (Euclidean distance)

Output:   
For each centroid, sum of the points assigned to it AND no. of points assigned to it

**reducer.py**   
For each centroid, aggregate the sums and counts from each mapper   
Update the location of the centroid as mean (i.e. sum / count) of the points assigned to it

Output:   
Updated location of each centroid

**Iterate *mapper.py* and *reducer.py* until converged (i.e. movement of centroids < threshold)**  
**If not yet converged, update *centroids.txt* with the outputs from previous reducer**

**display.py**   
Final location of each centroid and the number of points assigned to it
