#Operacoes
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans


total_cores = 7



photo = Image.open("girl.jpg")

photo = photo.resize((100,100))

pixels = np.array(photo)

#print(pixels.shape)

pixels_flat = pixels.reshape(-1, 3)

kmeans = KMeans(n_clusters=total_cores)

kmeans.fit(pixels_flat)

pixels_round = kmeans.cluster_centers_

pixels_round = pixels_round.astype(int)

print(pixels_round)

hex_colors = []

for rgb in pixels_round:
    hex_colors.append(f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")

print(hex_colors)

# ---------- Grafico ----------

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

graph = plt.figure()
plt.suptitle("Image Color Palette Analysis")

# ---------- 1 ----------

ax1 = graph.add_subplot(2, 2, 1) 
ax1.set_title("Resized Input Image") 
ax1.imshow(photo)

# ---------- 2 ----------

ax2 = graph.add_subplot(2, 2, 2, projection="3d") 
ax2.set_title("RGB Color Space Distribution")

for cont in range(total_cores):
    cluster_pixels = pixels_flat[kmeans.labels_ == cont]
    indices = np.random.choice(len(cluster_pixels), size=25, replace=False)
    amostra = cluster_pixels[indices]
    r = amostra[:, 0]
    g = amostra[:, 1]
    b = amostra[:, 2]
    ax2.scatter(r, g, b, c=hex_colors[cont])

ax2.set_xlabel("R")
ax2.set_ylabel("G")
ax2.set_zlabel("B")

# ---------- 3 ----------

ax3 = graph.add_subplot(2, 2, 3)     
ax3.set_title("Cluster Size Comparison")

quantity = []
for cont in range(total_cores):
    quantity.append(len(pixels_flat[kmeans.labels_ == cont]))

ax3.bar(hex_colors, quantity, color=hex_colors)
plt.xticks(rotation=45) 

# ---------- 4 ----------

ax4 = graph.add_subplot(2, 2, 4)
ax4.set_title("Dominant Color Percentage") 

ax4.pie(quantity, autopct='%1.1f%%', pctdistance=1.25, colors=hex_colors)
#labels=hex_colors

# ---------- Print ----------

plt.tight_layout()
plt.show()