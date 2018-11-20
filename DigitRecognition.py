import gzip
import numpy as np
import matplotlib.pyplot as plt

# Unzip contents and read the file
with gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb') as f:
    file_content = f.read()

# get the bytes from the file
file_content[0:4]

# read one image as a byte array
l = file_content[16:800]

image = ~np.array(list(file_content[16:800])).reshape(28,28).astype(np.uint8)

plt.imshow(image, cmap='gray')

with gzip.open('data/t10k-labels-idx1-ubyte.gz', 'rb') as f:
    labels = f.read()

int.from_bytes(labels[8:9], byteorder="big")