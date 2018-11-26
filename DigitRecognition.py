# Tkinter is Python's de-facto standard GUI (Graphical User Interface) package.
import tkinter as tk

import keras as kr
import numpy as np
import matplotlib.pyplot as plt
import math
import sklearn.preprocessing as pre
import gzip

from PIL import ImageTk, Image, ImageDraw, ImageFilter
import PIL

width = 280
height = 280
center = height//2
white = (255, 255, 255)
black = (0,0,0)

def nueralNet(img):

    global model, result

    # Read in images for training
    with gzip.open('data/train-images-idx3-ubyte.gz', 'rb') as f:
        train_img = f.read()

    # read in labels for training
    with gzip.open('data/train-labels-idx1-ubyte.gz', 'rb') as f:
        train_lbl = f.read()

    with gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb') as f:
        test_img = f.read()

    with gzip.open('data/t10k-labels-idx1-ubyte.gz', 'rb') as f:
        test_lbl = f.read()

    # Add a hidden layer with 1000 neurons and an input layer with 784.
    model.add(kr.layers.Dense(512, input_dim=784, activation="relu", kernel_initializer="normal"))

    model.add(kr.layers.Dense(10, activation="softmax", kernel_initializer="normal"))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # reshape the images and labels into 28x28 arrays.
    train_img = ~np.array(list(train_img[16:])).reshape(60000, 1, 784).astype(np.uint8)
    train_lbl =  np.array(list(train_lbl[ 8:])).astype(np.uint8)

    train_img = train_img/ 255
    train_lbl = kr.utils.to_categorical(train_lbl)

    # reshape the image array
    inputs = train_img.reshape(60000, 784)
    # Binarize labels in a one-vs-all fashion
    encoder = pre.LabelBinarizer()

    # Trains the model for a fixed number of epochs (iterations on a dataset).
    encoder.fit(train_lbl)
    outputs = encoder.transform(train_lbl)

    # Train the model
    model.fit(inputs, outputs, epochs=5, batch_size=1000)

    test_img = ~np.array(list(test_img[16:])).reshape(10000, 784).astype(np.uint8) / 255.0
    test_lbl =  np.array(list(test_lbl[ 8:])).astype(np.uint8)
    
    img =  np.array(list(img)).reshape(1,784)

    # for testing the encoder
    # for i in range(10):
    #    print(i, encoder.transform([i]))

    print(model.predict_classes(img))
    result.config(text='You Wrote the Number '+str(model.predict_classes(img)))


def clearCanvas(event):
    
    global image1, draw

    cv.delete("all")
    image1 = PIL.Image.new("RGB", (width, height), black)
    draw = ImageDraw.Draw(image1)
    

def save():

    global image1

    img = image1.resize((28, 28), Image.BICUBIC)
    img.save("image.png")
    
    img = imageprepare('image.png')

    nueralNet(img)
    

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="black",width=12)
    draw.line([x1, y1, x2, y2],fill="white",width=12)

def imageprepare(argv):

    im = Image.open(argv).convert('L')
    # im.show()

    tv = list(im.getdata())

    # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    tv = [(255 - x) * 1.0 / 255.0 for x in tv]
    
    return tv

# Start a neural network, building it by layers.
# using sequential model
model = kr.models.Sequential()

image1 = PIL.Image.new("RGB", (width, height), black)
draw = ImageDraw.Draw(image1)

# set the position of the windows
root = tk.Tk()
root.geometry("+{xPos}+{yPos}".format(xPos = 0, yPos = 0))

# Tkinter create a canvas to draw on
cv = tk.Canvas(root, width=width, height=height, bg='white')

# pack the gui
cv.pack()
cv.bind("<B1-Motion>", paint)
cv.bind('<Button-3>', clearCanvas)

# create text and buttons
button = tk.Button(text="Check Number",command=save)
text1 = tk.Label(text="Left Click Draw")
text2 = tk.Label(text="Right Click Clear")
result = tk.Label(text="You have not Checked a Number yet")

text1.pack()
text2.pack()
button.pack()
result.pack()

root.mainloop()