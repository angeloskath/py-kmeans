Python K-Means clustering
=========================

This small python module provides a simple interface for the K-Means
clustering algorithm.

Why
----

This module is a product of frustration with the clustering functions of
matlab and the general difficulty of handling large integer values instead
of doubles.

Although I started it because I wanted to cluster some integers in the
hamming space and matlab kept annoying me and scipy simply doesn't have
any other distance measure except for euclidean distance, the main
point while developing this was the decoupling of the K Means logic from
the data domain.

Usage
------

If your data are either in R^n or in hamming space then you can simply
pass the data, some centroids and a cutoff value to cluster them.

``` python
points = [[random.random()*10,random.random()*10] for _ in range(10)]
points.extend([[random.random()*10+10,random.random()*10+10] for _ in range(10)])

# I pass the first two points as the initial centroids
# you can either do this or simply pass two random points
kme = kmeans_euclid(points,points[:2],0.1)

# for hamming space use kmeans_hamming()
```

Custom data
-----------

The whole point as I mentioned above, was to decouple the data from the
K-Means logic. The main function `kmeans` receives two extra parameters
**distf** and **centroidf**. **distf** is a function that returns a measure
of distance between two datapoints. **centroidf** is a function that
receives a list of data points and returns a data point to be the
centroid of the points passed as parameters.

Euclidean distance and euclidean geometric mean as well as hamming
distance and hamming mean are both implemented.
