import random

# generate random points
random_pts = []
while len(random_pts) < 10:
    id = random.randint(0, 60000)
    if not id in random_pts:
        random_pts.append(id)

with open('centroids.txt', 'w') as file1:
    cid = 0
    with open('train-images', 'r') as file2:
        for line in file2:
            id, image = line.strip().split('\t', 1)
            if int(id) in random_pts:
                file1.write(str(cid) + '\t' + image + '\n')
                cid += 1