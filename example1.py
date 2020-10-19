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
        self.fun2 = lambda x: cv.Canny(x, 60, 130)
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