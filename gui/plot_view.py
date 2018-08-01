# -*- coding: utf-8 -*-
"""

@author:  Stig Rune Sellevag <stig-rune.sellevag@ffi.no>
@warning: No warranty offered.
@date:    Mon Mar 28 16:48:49 2016
"""

import Tkinter as Tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class PlotView:
    def __init__(self, master):
        self.master = master
        self.init()

    def init(self):
        """Function for initializing the plot view."""
        self.frame = Tk.Frame(self.master)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.grid(
            row=1, column=1, columnspan=2, rowspan=4, sticky="nsew"
        )

        self.fig = Figure(figsize=(12, 7.5))
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().grid(
            row=1, column=1, padx=5, pady=2, sticky="nsew"
        )
        self.canvas.show()

        self.toolbar_frame = Tk.Frame(self.master)
        self.toolbar_frame.rowconfigure(5, weight=1)
        self.toolbar_frame.grid(row=5, column=1, padx=5, sticky="nw")
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.toolbar_frame)
        self.toolbar.update()


