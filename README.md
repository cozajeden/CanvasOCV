# CanvasOCV
Canvas widget for tkinter that displays images in numpy/OpenCV array format.

## Requirements
'pip install Pillow numpy tk threaded opencv-python'



Use set_imageOCV(image) method to display an image.


'''python

    from threading import Thread

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
            
        def camera(self):
            while True:
                ret, frame = self.cap.read()
                self.canvas.set_imageOCV(frame)

        def destroy(self):
            self.cap.release()
            super().destroy()

    root = MyTk()
    root.mainloop()
'''
