# -*- coding: utf-8 -*-
"""
Script for freezing the Argos Viewer code.

@author:  Stig Rune Sellevag <stig-rune.sellevag@ffi.no>
@warning: No warranty offered.
@date:    Tue Mar 29 09:54:43 2016
"""

from cx_Freeze import setup
from cx_Freeze import Executable

import sys

# Dependencies are automatically detected, but it might need
# fine tuning.

target_name = "argosviewer.exe"

shortcut_table = [
                ("DesktopShortcut",
                 "DesktopFolder",
                 "CENSIT",
                 "TARGETDIR",
                 "[TARGETDIR]" + target_name,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 "TARGETDIR")
]

msi_data = { "Shortcut": shortcut_table}

options = {
    "build_exe": {
        "compressed": True,
        "packages": [],
        "excludes": [],
        "includes": ["scipy.special._ufuncs_cxx",
                     "scipy.linalg",
                     "scipy.integrate.vode",
                     "scipy.integrate.lsoda",
                     "matplotlib.backends.backend_qt4agg",
                     "FileDialog"],
        "include_files": ["ffi_logo.png",
                          "data/"]
    },
    "bdist_msi": {
        "data": msi_data
    }
}

base = "Win32GUI" if sys.platform == "win32" else None

executables = [
    Executable(script="main.pyw",
               base=base,
               targetName=target_name)
]

setup(name="ArgosViewer",
      version = "0.1",
      description = "Argos Viewer",
      options     = options,
      executables = executables
)

