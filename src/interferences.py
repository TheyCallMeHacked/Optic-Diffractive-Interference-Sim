import tkinter as tk
from extfuncs import *

window = tk.Tk()

window.columnconfigure(0, weight=1, minsize=300)
window.rowconfigure(0, weight=1, minsize=300)

# Frame with the main content.
content = tk.Frame(
    window,
)
content.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")

# Frame for padding apparently necessary to have the resized Frame
pad_frame = tk.Frame(content, borderwidth=0, width=200, height=200)
pad_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
# Frame with the plot. It lays inside the "content" Frame
plot_frame = tk.Frame(
    content,
    bg = "blue",
    width = 300,
    height = 300
)
# calls function to fix the aspect ratio
set_aspect(plot_frame, pad_frame, aspect_ratio=1) 
content.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)

# the matplotlib stuff
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np

fig = Figure(figsize=(5, 4), dpi=100)
xpix, ypix = 100, 100

pic = [[hsv2rgb(0, 1, np.interp(wave(j, i, xpix, f=1/7.5), [-2,2], [0,1])) for j in range(xpix)] for i in range(ypix)]
graph = fig.add_subplot(111).imshow(pic)

canvas = FigureCanvasTkAgg(fig, master=plot_frame)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

wlc = 0
wlf = 1
noise_y = 0


def update_wavelength(f):
    global wlc, wlf
    wlc = np.interp(f, [380, 750], [2/3, 0])
    wlf = np.interp(f, [380, 750], [1/3.8, 1/7.5])
    pic = [[hsv2rgb(wlc, 1, np.interp(wave(j, i, xpix, f=wlf), [-2,2], [0,1])) for j in range(xpix)] for i in range(ypix)]
    graph.set_data(pic)
    canvas.draw()

"""def update_xoff(f):
    global noise_x
    noise_x = int(f)
    graph.set_data([pic[noise_h][i+noise_y][noise_x:noise_x+50] for i in range(50)])
    canvas.draw()

def update_yoff(f):
    global noise_y
    noise_y = int(f)
    graph.set_data([pic[noise_h][i+noise_y][noise_x:noise_x+50] for i in range(50)])
    canvas.draw()"""

# Frame containing the setting controls
window.columnconfigure(1, weight=0, minsize=300)
settings = tk.Frame(
    window,
    bg = "red"
)
settings.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")

wavel = tk.Scale(settings, from_=380, to=750, resolution=1, orient=tk.HORIZONTAL, label="Longueur d'onde (de 380nm à 750nm)", command=update_wavelength)
wavel.set(750)
wavel.pack(side=tk.TOP, fill=tk.X)

"""xoff = tk.Scale(settings, from_=0, to=49, resolution=1, orient=tk.HORIZONTAL, label="X Offset (from 0 to 49)", command=update_xoff)
xoff.set(25)
xoff.pack(side=tk.TOP, fill=tk.X)

yoff = tk.Scale(settings, from_=0, to=49, resolution=1, orient=tk.HORIZONTAL, label="Y Offset (from 0 to 49)", command=update_yoff)
yoff.set(25)
yoff.pack(side=tk.TOP, fill=tk.X)"""

# usual Tkinter stuff
center(window)
window.title("Interférences")
window.mainloop()
