# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from PyInstaller.utils.hooks import collect_all, collect_submodules

block_cipher = None

# Collect all gi (PyGObject) related files
gi_datas, gi_binaries, gi_hiddenimports = collect_all('gi')

# Add hidden imports for GTK
hiddenimports = [
    'gi',
    'gi.repository.Gtk',
    'gi.repository.Gdk', 
    'gi.repository.GObject',
    'gi.repository.GLib',
    'gi.repository.Pango',
    'gi.repository.PangoCairo',
    'gi.repository.GdkPixbuf',
    'cairo',
    'pycairo',
]
hiddenimports.extend(gi_hiddenimports)

# Data files - include the data folder
datas = [
    ('data', 'data'),
    ('apx', 'apx'),
]
datas.extend(gi_datas)

a = Analysis(
    ['bin/apx'],
    pathex=[],
    binaries=gi_binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='APX',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to True if you want to see console output for debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='APX',
)
