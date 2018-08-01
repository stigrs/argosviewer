# -*- coding: utf-8 -*-
"""
Controller class for Argos Viewer.

@author:  Stig Rune Sellevag <stig-rune.sellevag@ffi.no>
@warning: No warranty offered.
@date:    Fri Mar 25 11:15:34 2016
"""

import Tkinter as Tk
import tkMessageBox
import tkFileDialog
import traceback as tb
from about import about
from gui.view import View
from lib.argos import Argos

class Controller:
    def __init__(self):
        """Initialize controller."""
        self.root  = Tk.Tk()
        self.view  = View(self.root)
        self.argos = Argos()

        self.pulldown_menu()

        self.view.toolbar.reset_button.bind("<Button>", self.reset)
        self.view.toolbar.plot_button.bind("<Button>", self.plot)

        self.view.edit.rot_scale.bind("<ButtonRelease-1>", self.edit_rot)
        self.view.edit.rot_entry.bind("<Return>", self.edit_rot)
        self.view.edit.x_shift.bind("<ButtonRelease-1>", self.edit_x_shift)
        self.view.edit.dx_entry.bind("<Return>", self.edit_x_shift)
        self.view.edit.y_shift.bind("<ButtonRelease-1>", self.edit_y_shift)
        self.view.edit.dy_entry.bind("<Return>", self.edit_y_shift)   
             
    def about(self):
        """Display about message."""
        tkMessageBox.showinfo("About", about())

    def pulldown_menu(self):
        """Create pulldown menubar."""
        self.view.menubar.filemenu.add_command(
            label="Load", command=self.load
        )
        self.view.menubar.filemenu.add_command(
            label="Save as", command=self.save
        )
        self.view.menubar.filemenu.add_separator()
        self.view.menubar.filemenu.add_command(
            label="Exit", underline=1, command=self.quit
        )
        self.view.menubar.helpmenu.add_command(
            label="About", command=self.about
        )

    def load(self):
        """Load Argos data from file."""
        filename = tkFileDialog.askopenfilename(
            title="Load Argos GRD file",
            filetypes=[("GRD files", "*.grd")]
        )
        self.argos.load_grd(filename)

    def save(self):
        """Save data to Argos GRD file."""
        filename = tkFileDialog.asksaveasfilename(
            title="Save Argos GRD file",
            defaultextension=".grd",
            filetypes=[("GRD files", "*.grd")]
        )
        self.argos.save_grd(
            filename, self.view.edit.rot.get(), self.view.edit.dx.get(),
            self.view.edit.dy.get()
        )
        
    def edit_rot(self, event):
        """Edit rotation."""
        if int(event.type) == 5: # <ButtonRelease-1>
            rot = self.view.edit.rot_scale.get()
            self.view.edit.rot.set(rot)
        if int(event.type) == 2: # <Return>
            rot = self.view.edit.rot.get()
            self.view.edit.rot_scale.set(rot)

    def edit_x_shift(self, event):
        """Edit X shift."""
        if int(event.type) == 5: # <ButtonRelease-1>
            dx = self.view.edit.x_shift.get()
            self.view.edit.dx.set(dx)
        if int(event.type) == 2: # <Return>
            dx = self.view.edit.dx.get()
            self.view.edit.x_shift.set(dx)

    def edit_y_shift(self, event):
        """Edit Y shift."""
        if int(event.type) == 5: # <ButtonRelease-1>
            dy = self.view.edit.y_shift.get()
            self.view.edit.dy.set(dy)
        if int(event.type) == 2: # <Return>
            dy = self.view.edit.dy.get()
            self.view.edit.y_shift.set(dy)
            
    def plot(self, event):
        self.view.plot.init()
        try:
            self.argos.plot_grd(
                self.view.plot.fig, self.view.plot.ax, 
                self.view.edit.rot.get(), self.view.edit.dx.get(),
                self.view.edit.dy.get()
            )
            self.view.plot.canvas.show()
        except Exception:
            tkMessageBox.showerror("Error", tb.format_exc())
        
    def reset(self, event):
        """Reset plot view and edit settings."""
        self.view.plot.init()
        self.view.edit.rot.set(0)
        self.view.edit.rot_scale.set(0)
        self.view.edit.dx.set(0)
        self.view.edit.x_shift.set(0)
        self.view.edit.dy.set(0)
        self.view.edit.y_shift.set(0)
        
    def run(self):
        """This is the main loop for running ArgosViewer controller."""
        try:
            self.root.title("Argos Viewer")
            self.root.deiconify()
            self.root.columnconfigure(0, weight=1)
            self.root.columnconfigure(1, weight=1)
            self.root.rowconfigure(0, weight=1)
            self.root.rowconfigure(1, weight=1)
            self.root.rowconfigure(2, weight=1)
            self.root.rowconfigure(3, weight=1)
            self.root.rowconfigure(4, weight=1)
            self.root.mainloop()
        except Exception as err:
            tkMessageBox.showerror("Error", repr(err))

    def quit(self):
        """Quit the application."""
        self.root.destroy()
