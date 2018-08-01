# -*- coding: utf-8 -*-
"""
Class providing view of editing methods for Argos Viewer.

@author:  Stig Rune Sellevag <stig-rune.sellevag@ffi.no>
@warning: No warranty offered.
@date:    Tue Mar 29 07:46:44 2016
"""

import Tkinter as Tk

class EditView:
    def __init__(self, master):
        self.frame  = Tk.Frame(master)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.grid(row=1, column=0, rowspan=3, pady=5, sticky="nsew")

        self._edit_rot()
        self._edit_x_shift()
        self._edit_y_shift()
        
    def _edit_rot(self):
        self.frame1 = Tk.LabelFrame(self.frame, text="Rotation")
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.grid(row=0, column=0, sticky="ew")
        
        self.rot_scale = Tk.Scale(
            self.frame1, orient=Tk.HORIZONTAL, from_=0.0, to=360.0,
            resolution=1.0
        )
        self.rot_scale.grid(
            row=1, column=0, columnspan=2, padx=2, pady=5, sticky="ew"
        )
        self.rot = Tk.DoubleVar()
        self.rot.set(self.rot_scale.get())
        self.rot_entry = Tk.Entry(self.frame1, textvariable=self.rot)
        self.rot_entry.config(justify=Tk.RIGHT, width=5)
        self.rot_entry.grid(row=0, column=0, padx=2, sticky="e")
        
        label = Tk.Label(self.frame1, text="degrees")
        label.grid(row=0, column=1, padx=2, sticky="w")

    def _edit_x_shift(self):        
        self.frame2 = Tk.LabelFrame(self.frame, text="Shift X direction")
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.grid(row=1, column=0, sticky="ew")
        
        self.x_shift = Tk.Scale(
            self.frame2, orient=Tk.HORIZONTAL, from_=-100, to=100, resolution=1        
        )
        self.x_shift.grid(
            row=1, column=0, columnspan=2, padx=2, pady=5, sticky="ew"        
        )
        self.dx = Tk.IntVar()
        self.dx.set(self.x_shift.get())
        self.dx_entry = Tk.Entry(self.frame2, textvariable=self.dx)
        self.dx_entry.config(justify=Tk.RIGHT, width=5)
        self.dx_entry.grid(row=0, column=0, padx=2, sticky="e")        

        label = Tk.Label(self.frame2, text="cells")
        label.grid(row=0, column=1, padx=2, sticky="w")

    def _edit_y_shift(self):
        self.frame3 = Tk.LabelFrame(self.frame, text="Shift Y direction")
        self.frame3.columnconfigure(0, weight=1)
        self.frame3.rowconfigure(0, weight=1)
        self.frame3.grid(row=2, column=0, sticky="ew")
        
        self.y_shift = Tk.Scale(
            self.frame3, orient=Tk.HORIZONTAL, from_=-100, to=100, resolution=1        
        )
        self.y_shift.grid(
            row=1, column=0, columnspan=2, padx=2, pady=5, sticky="ew"        
        )
        self.dy = Tk.IntVar()
        self.dy.set(self.y_shift.get())
        self.dy_entry = Tk.Entry(self.frame3, textvariable=self.dy)
        self.dy_entry.config(justify=Tk.RIGHT, width=5)
        self.dy_entry.grid(row=0, column=0, padx=2, sticky="e")        

        label = Tk.Label(self.frame3, text="cells")
        label.grid(row=0, column=1, padx=2, sticky="w")
        