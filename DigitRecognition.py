import tkinter as tk
# Tkinter is Python's de-facto standard GUI (Graphical User Interface) package.

def clearCoords(event):
    # when left click released, remove the old coordinates so you can draw multiple non conjoined lines
    # Without this, if you draw a seven or some letters, it would draw a continuous line, unbroken
    canvas.old_coords = None

def clearCanvas(event):
    canvas.old_coords = None
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

root = tk.Tk()

# show a canvas page
canvas = tk.Canvas(root, width=400, height=400)
# pack the canvas to be show
canvas.pack()
# set the old coords as null
canvas.old_coords = None

# If the left mouse button held, Run the function that will draw a line
root.bind('<B1-Motion>', draw)
# If the right mouse button pressed, Run the function that clear the canvas
root.bind('<Button-3>', clearCanvas)
# When 
root.bind('<ButtonRelease-1>', clearCoords)
# loop 
root.mainloop()