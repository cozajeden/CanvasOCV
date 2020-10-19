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