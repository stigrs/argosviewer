# -*- coding: utf-8 -*-
"""
Module providing driver for Argos Viewer.

@author:  Stig Rune Sellevag <stig-rune.sellevag@ffi.no>
@warning: No warranty offered.
@date:    Fri Mar 25 10:41:50 2016
"""

from controller import Controller

def main():
    """Driver for ArgosViewer."""
    app = Controller()
    app.run()

if __name__ == "__main__":
    main()
    