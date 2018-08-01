# -*- coding: utf-8 -*-
"""
Class providing view of toolbar.

@author:  Stig Rune Sellevag <stig-rune.sellevag@ffi.no>
@warning: No warranty offered.
@date:    Mon Mar 28 17:06:35 2016
"""

import Tkinter as Tk

class ToolBarView:
    def __init__(self, master):
        self.frame = Tk.LabelFrame(master)
        self.frame.grid(row=0, column=0, columnspan=3, sticky="ew")

        self.frame1 = Tk.Frame(self.frame)
        self.frame1.grid(row=0, column=0, sticky="w")

        self.reset_button = Tk.Button(
            self.frame1, text="Reset", relief="raised", width=10
        )
        self.reset_button.grid(row=0, column=0, sticky="ew")

        self.plot_button = Tk.Button(
            self.frame1, text="Plot", relief="raised", width=10
        )
        self.plot_button.grid(row=0, column=1, sticky="ew")

