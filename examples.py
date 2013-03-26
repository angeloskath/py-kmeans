
import random
from kmeans import kmeans_euclid,kmeans_hamming

def plot2d(data,centroids,data_to_centroids):
	xs = lambda d: map(lambda x: x[0],d)
	ys = lambda d: map(lambda x: x[1],d)
	
	colors = ['red','blue']
	for c,centroid in enumerate(centroids):
		d = map(
			lambda i: data[i[0]],
			filter(
				lambda x: x[1]==c,
				enumerate(data_to_centroids)
			)
		)
		plt.scatter(xs(d),ys(d),marker='o',c=colors[c])
		plt.scatter([centroid[0]],[centroid[1]],s=80,marker='x',c='yellow')
	
	plt.show()

def plot_hist(data_to_centroids):
	plt.hist(data_to_centroids,bins=range(max(data_to_centroids)+2))
	plt.show()

try:
	from matplotlib import pyplot as plt
except:
	plot2d = lambda a,b,c: None
	plot_hist = lambda a: None

print "Generating 20 2d points split in two obvious clusters";
points = [[random.random()*10,random.random()*10] for _ in range(10)]
points.extend([[random.random()*10+10,random.random()*10+10] for _ in range(10)])

print "Clustering with euclidean distance"
kme = kmeans_euclid(points,points[:2],0.1)

plot2d(points,kme[0],kme[1])

print "Generate 200 random 64bit integers"
numbers = [int(random.random()*2**64) for _ in range(200)]

print "Clustering with hamming distance"
kmh = kmeans_hamming(numbers,numbers[:5],0)

plot_hist(kmh[1])

# this annoying thing because matplotlib won't show otherwise
print "Enter to exit"
raw_input()
