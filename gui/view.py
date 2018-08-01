# -*- coding: utf-8 -*-
"""
Class providing main view for Argos Viewer.

@author:  Stig Rune Sellevag <stig-rune.sellevag@ffi.no>
@warning: No warranty offered.
@date:    Fri Mar 25 11:11:39 2016
"""

import Tkinter as Tk
from menu_view import MenuView
from toolbar_view import ToolBarView
from plot_view import PlotView
from edit_view import EditView
from logo_view import LogoView

class View:
    def __init__(self, master):
        self.frame = Tk.Frame(master)
        self.frame.grid(sticky="nsew")

        self.menubar  = MenuView(master)
        self.toolbar  = ToolBarView(master)
        self.plot     = PlotView(master)
        self.edit     = EditView(master)
        self.logo     = LogoView(master, "ffi_logo.png")

        master.config(menu=self.menubar)
