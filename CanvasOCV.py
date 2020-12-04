import cv2 as cv
from tkinter import *
from PIL import Image, ImageTk

class CanvasOCV(Canvas):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.imageArray = None
        self.imageFromArray = None
        self.imageResized = None
        self.imageTk = None
        self.outputImage = None
        self.bind('<Configure>', self.__redraw_canvas__)

    def set_imageOCV(self, image):
        if len(image.shape) > 2:
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        self.imageArray = image
        self.__from_array__()
        self.__redraw_canvas__()

    def __from_array__(self):
        """Change format from numpy.array to PIL.Image"""
        if self.imageArray is not None:
            self.imageFromArray = Image.fromarray(self.imageArray)

    def __redraw_canvas__(self, *args, **kwargs):
        """Calculate new image size, draw new image, clean background."""
        if self.imageFromArray is not None:
            # Get Canvas and input Image dimensions
            width, height = self.winfo_width(), self.winfo_height()
            iwidth, iheight = self.imageFromArray.size
            if width > 1 and height > 1:   
                # Calculate new Image dimensions
                cratio = height/width
                iratio = iheight/iwidth
                if cratio >= iratio:
                    iheight = int(width * iratio)
                    iwidth = width
                else:
                    iwidth = int(height / iratio)
                    iheight = height

                # Resize, convert to ImageTk and draw
                self.imageResized = self.imageFromArray.resize((iwidth, iheight), Image.ANTIALIAS)
                image = ImageTk.PhotoImage(self.imageResized)
                self.outputImage = self.create_image(iwidth/2, iheight/2, image=image)
                # Delete everything else from canvas (To not stack images)
                to_delete = list(self.find_withtag(ALL))
                to_delete.pop(to_delete.index(self.outputImage))
                self.delete(to_delete)
                self.imageTk = image
                # You can add other items to draw below.