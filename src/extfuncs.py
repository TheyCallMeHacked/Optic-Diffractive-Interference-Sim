import numpy as np

def center(main, w = None, h = None):
    main.title("Our Program")
    main.update_idletasks()
    width = w if w else main.winfo_width()
    height = h if h else main.winfo_height()
    x = (main.winfo_screenwidth() - width) // 2
    y = (main.winfo_screenheight() - height) // 2
    main.geometry("{}x{}+{}+{}".format(width, height, x, y))
    main.minsize(width, height)

def set_aspect(content_frame, pad_frame, aspect_ratio):
    # a function which places a frame within a containing frame, and
    # then forces the inner frame to keep a specific aspect ratio

    def enforce_aspect_ratio(event):
        # when the pad window resizes, fit the content into it,
        # either by fixing the width or the height and then
        # adjusting the height or width based on the aspect ratio.

        # start by using the width as the controlling dimension
        desired_width = event.width
        desired_height = int(event.width / aspect_ratio)

        # if the window is too tall to fit, use the height as
        # the controlling dimension
        if desired_height > event.height:
            desired_height = event.height
            desired_width = int(event.height * aspect_ratio)

        # place the window, giving it an explicit size
        content_frame.place(in_=pad_frame, x=0, y=0, 
            width=desired_width, height=desired_height)

    pad_frame.bind("<Configure>", enforce_aspect_ratio)

def wave(x, y, mx, s=30, f=1, t=0):
    r1 = np.sqrt(y*y + (x-(mx/2) + s/2)**2)
    r2 = np.sqrt(y*y + (x-(mx/2) - s/2)**2)
    return np.cos(2*np.pi * f * (t - r1)) + np.cos(2*np.pi * f * (t - r2))

def genpattern(xsize, ysize, s=30, f=1, t=0, c=0):
    out = np.empty((ysize, xsize, 3))
    for i in range(xsize//2):
        for j in range(ysize):
            out[j][i] = hsv2rgb(c, 1, np.interp(wave(i, j, xsize, s, f, t), [-2,2], [0,1])) #hsv2rgb(c, 1, np.interp(wave(j, i, xsize, s, f, t), [-2,2], [0,1]))
            out[j][-i-1] = out[j][i]
        #out[i] = [hsv2rgb(c, 1, np.interp(wave(j, i, xsize, s, f, t), [-2,2], [0,1])) for j in range(xsize)]
        #print(out[i])
        #out[i] += out[i][::-1]
    return out


def hsv2rgb(h, s, v):
    i = np.floor(h*6)
    f = h*6 - i
    p = v * (1-s)
    q = v * (1-f*s)
    t = v * (1-(1-f)*s)

    r, g, b = [
        (v, t, p),
        (q, v, p),
        (p, v, t),
        (p, q, v),
        (t, p, v),
        (v, p, q),
    ][int(i%6)]

    return r, g, b
