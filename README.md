![APX gameplay](https://farm8.staticflickr.com/7434/13823878335_e242ac1c23_o.png)


Game Description and Goal
=========================

APX is a [QIX](http://en.wikipedia.org/wiki/Qix) clone with minor differences in gameplay from the original.

Use arrow keys to move around the perimeter of square, hold down Space or Shift  
to cut into the area. Connect back to perimeter to claim the area.

Your objective is to claim 75% or more to proceed to the next level.

Claiming with Shift key will be slower but give you double the points.

For every claimed full percent over 75% you get extra 1000 points.


Controls
========

| Key | Action |
|-----|--------|
| Arrow Keys | Move around the perimeter |
| Space / Shift | Cut into the area (hold down) |
| Shift | Slow mode (double points) |
| P | Pause game |
| F11 | Toggle fullscreen |
| ESC | Exit fullscreen |


Running on Linux
================

The game requires GTK 3.0 with Python introspection installed.
Your safest bet would be to run GNOME Shell, or being able to run GNOME Shell.

```bash
# Install dependencies (Debian/Ubuntu)
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0

# Run the game
python bin/apx
```


Running on Windows (MSYS2)
==========================

The game requires MSYS2 with GTK3 and PyGObject installed.

### Step 1: Install MSYS2

Download and install MSYS2 from https://www.msys2.org/

Install to the default location: `C:\msys64`

### Step 2: Install Dependencies

Open **"MSYS2 MINGW64"** terminal (not just "MSYS2") and run:

```bash
# Update MSYS2
pacman -Syu

# Install Python, GTK3, and PyGObject
pacman -S mingw-w64-x86_64-python mingw-w64-x86_64-python-gobject mingw-w64-x86_64-gtk3
```

### Step 3: Run the Game

Navigate to the game directory and run:

```bash
cd /g/Jogos/pyqix  # Adjust path as needed
python bin/apx
```


Building Windows Executable
===========================

You can create a standalone Windows executable using PyInstaller from within MSYS2.

### Step 1: Install PyInstaller

In the **MSYS2 MINGW64** terminal:

```bash
pacman -S mingw-w64-x86_64-python-pip
python -m pip install pyinstaller
```

### Step 2: Build the Executable

```bash
cd /g/Jogos/pyqix  # Adjust path as needed
python -m PyInstaller apx.spec
```

The executable will be created at `dist/APX/APX.exe`.

### Rebuilding After Changes

If you make changes to the code, rebuild with:

```bash
python -m PyInstaller apx.spec --clean
```


Implementation
==============

The game was implemented using 
[hamster graphics](https://github.com/projecthamster/experiments)
and somewhat serves also as a tech demo. Check out the tutorial!


License
=======

See [LICENSE](LICENSE) file for details.
# QIX
