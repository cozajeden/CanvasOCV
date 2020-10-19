# CanvasOCV
Canvas widget for tkinter that displays images in numpy/OpenCV array format.

## Requirements
**threaded is required only for an example**
```
pip install Pillow numpy tk threaded opencv-python
```
## Examples
Use `set_imageOCV(`_image_`)` method to display an image.

> ### 1. Display live image from camera
Click the 'Change display mode' button to swap display mode.
```python
from threading import Thread
from CanvasOCV import CanvasOCV
from tkinter import *
import cv2 as cv

class MyTk(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cap = cv.VideoCapture(0, cv.CAP_DSHOW)
        self.frame = Frame(self)
        self.frame.pack(fill=BOTH, expand=True)
        self.canvas = CanvasOCV(self.frame)
        self.canvas.pack(fill=BOTH, expand=True)
        self.thread = Thread(name='camera', target=self.camera)
        self.thread.daemon = True
        self.thread.start()
        self.fun1 = lambda x: x
        self.fun2 = lambda x: cv.Canny(x, 80, 130)
        self.button = Button(self, text='Change display mode', font='Times 20 bold', command=self.swap)
        self.button.pack(side=BOTTOM)

    def swap(self):
        self.fun1, self.fun2 = self.fun2, self.fun1
        
    def camera(self):
        while True:
            ret, frame = self.cap.read()
            frame = self.fun1(frame)
            self.canvas.set_imageOCV(frame)

    def destroy(self):
        self.cap.release()
        super().destroy()

root = MyTk()
root.mainloop()
```

> ### 2. Display image from file.
You will be prompt to choose an image after running this example.
```python
from CanvasOCV import CanvasOCV
from tkinter import *
from tkinter.filedialog import askopenfilename
import cv2 as cv

class MyTk(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame = Frame(self)
        self.frame.pack(fill=BOTH, expand=True)
        self.canvas = CanvasOCV(self.frame)
        self.canvas.pack(fill=BOTH, expand=True)
        self.camera()
        
    def camera(self):
        path = None
        while path is None:
            path = askopenfilename()
        image = cv.imread(path)
        self.canvas.set_imageOCV(image)

    def destroy(self):
        super().destroy()

root = MyTk()
root.mainloop()
```

## `Have fun with OpenCV in tkinter GUI!`