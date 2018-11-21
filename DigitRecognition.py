import tkinter as tk
# Tkinter is Python's de-facto standard GUI (Graphical User Interface) package.

def check():
    print('test')

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


# Main Window - canvas
root = tk.Tk()
# second window - control panel
second_win = tk.Toplevel(root)

# show a canvas page
canvas = tk.Canvas(root, width=400, height=400)
canvas2 = tk.Canvas(second_win, width=200, height=300)

# create text
canvas2.create_text(100,10,fill="darkblue",font="Times 12 italic bold", text="Left click to Draw")
canvas2.create_text(100,30,fill="darkblue",font="Times 12 italic bold", text="Right click to Clear")

# pack the canvas to be shown
canvas.pack()
canvas2.pack()

# Tkinter Button
B = tk.Button(second_win, text ="Check Value", command = check)
B.pack()

# set the position of the windows
root.geometry("+{xPos}+{yPos}".format(xPos = 0, yPos = 0))
second_win.geometry("+{xPos}+{yPos}".format(xPos = 400, yPos = 0))

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