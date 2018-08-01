# -*- coding: utf-8 -*-
"""
Class for viewing Logo.

@author:  Stig Rune Sellevag <stig-rune.sellevag@ffi.no>
@warning: No warranty offered.
@date:    Fri Mar 25 11:13:25 2016
"""

import Tkinter as Tk
from PIL import ImageTk
from PIL import Image

class LogoView:
    def __init__(self, master, image_file):
        self.frame = Tk.Frame(master)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(4, weight=1)
        self.frame.grid(row=4, column=0, sticky="new")

        img = ImageTk.PhotoImage(Image.open(image_file))
        label = Tk.Label(self.frame, image=img)
        label.image = img
        label.grid(sticky="nsew")

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)