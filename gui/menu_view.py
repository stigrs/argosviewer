# -*- coding: utf-8 -*-
"""
Class providing view of the menu bar.

@author:  Stig Rune Sellevag <stig-rune.sellevag@ffi.no>
@warning: No warranty offered.
@date:    Fri Mar 25 11:14:12 2016
"""

import Tkinter as Tk

class MenuView(Tk.Menu):
    def __init__(self, master):
        Tk.Menu.__init__(self, master)
        self.master   = master
        self.filemenu = Tk.Menu(master, tearoff=False)
        self.helpmenu = Tk.Menu(master, tearoff=False)

        self.add_cascade(label="File", underline=0, menu=self.filemenu)
        self.add_cascade(label="Help", underline=0, menu=self.helpmenu)