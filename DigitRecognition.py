# Tkinter is Python's de-facto standard GUI (Graphical User Interface) package.
import tkinter as tk
import keras as kr
import numpy as np
import matplotlib.pyplot as plt
import math
import sklearn.preprocessing as pre
import gzip
import skimage.io as ski_io

from skimage.transform import resize


def nueralNet(image):

    # Read in images for training
    with gzip.open('data/train-images-idx3-ubyte.gz', 'rb') as f:
        train_img = f.read()

    # read in labels for training
    with gzip.open('data/train-labels-idx1-ubyte.gz', 'rb') as f:
        train_lbl = f.read()

    # Start a neural network, building it by layers.
    # using sequential model
    model = kr.models.Sequential()
    # Add a hidden layer with 1000 neurons and an input layer with 784.
    model.add(kr.layers.Dense(units=1000, activation='relu', input_dim=784))
    # Add a three neuron output layer.
    model.add(kr.layers.Dense(units=10, activation='softmax'))
    
    model.compile(loss='categorical_crossentropy', optimizer='ADAM', metrics=['accuracy'])

    # reshape the images and labels into 28x28 arrays.
    train_img = ~np.array(list(train_img[16:])).reshape(60000, 28, 28).astype(np.uint8)
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
    model.fit(inputs, outputs, epochs=15, batch_size=10, verbose=1)
    # model.evaluate(test_img, test_lbl)

def check():
    # Button clicked and user intends to check a Digit from a Drawing
    canvas.update()

    # save canvas to .eps (postscript) file
    canvas.postscript(file="image.eps", colormode="gray")

    img = ski_io.imread('image.eps')

    print(img)
    # img_resized = cv2.resize(img, dsize=(212, 212), interpolation=cv2.INTER_NEAREST)

    # nueralNet(img_resized)


def checkFile():
    # Button clicked and user intends to check a Digit from a File
    print('test2')


def clearCoords(event):
    # when left click released, remove the old coordinates so you can draw multiple non conjoined lines
    # Without this, if you draw a seven or some letters, it would draw a continuous line, unbroken
    canvas.old_coords = None


def clearCanvas(event):
    # set the old coordinates to zero
    canvas.old_coords = None
    # clear everything from the canvas
    canvas.delete("all")


def draw(event):
    # set X and Y coordinates to the event X and Y.
    x, y = event.x, event.y
    # if the old coordinates have a value
    if canvas.old_coords:
        # set x1 and y1 coordinates to the old coordinates
        x1, y1 = canvas.old_coords
        # create a line, from the new coordinates, back to the old coordinates
        canvas.create_line(x, y, x1, y1)
    # set the old coordinates to the values that the new coordinates to be used as old coordinates, next iteration    
    canvas.old_coords = x, y


def main():
    print('Program Started')

if __name__ == "__main__":main()


# Main Window - canvas
root = tk.Tk()
# second window - control panel
second_win = tk.Toplevel(root)

# show a canvas page
canvas = tk.Canvas(root, width=560, height=560)
canvas2 = tk.Canvas(second_win, width=200, height=300)

# create text
canvas2.create_text(100,10,fill="darkblue",font="Times 12 italic bold", text="Left click to Draw")
canvas2.create_text(100,30,fill="darkblue",font="Times 12 italic bold", text="Right click to Clear")

# pack the canvas to be shown
canvas.pack()
canvas2.pack()

# Tkinter Button
B = tk.Button(second_win, text ="Check File", command = checkFile)
B.pack()

B2 = tk.Button(second_win, text ="Check Drawing", command = check)
B2.pack()

# set the position of the windows
root.geometry("+{xPos}+{yPos}".format(xPos = 0, yPos = 0))
second_win.geometry("+{xPos}+{yPos}".format(xPos = 561, yPos = 0))

# set the old coords as null
canvas.old_coords = None
# If the left mouse button held, Run the function that will draw a line
root.bind('<B1-Motion>', draw)
# If the right mouse button pressed, Run the function that clear the canvas
root.bind('<Button-3>', clearCanvas)
# When the left mouse button is released, reset the coordinates so you can break a line or draw multiple images
root.bind('<ButtonRelease-1>', clearCoords)
# loop
root.mainloop()