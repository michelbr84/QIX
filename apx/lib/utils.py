import os
import shutil
import sys

def install_font(font_filename):
    # Use expanduser for cross-platform home directory (works on Windows and Linux)
    home_dir = os.path.expanduser("~")
    fonts_dir = os.path.join(home_dir, '.fonts')
    if not os.path.exists(fonts_dir):
        os.makedirs(fonts_dir)

    font_path = os.path.join(fonts_dir, font_filename)
    if not os.path.exists(font_path):
        # Get the data directory - handle both development and PyInstaller frozen mode
        if getattr(sys, 'frozen', False):
            # Running as compiled executable
            base_dir = sys._MEIPASS
            data_dir = os.path.join(base_dir, 'data')
        else:
            # Running as script
            module_dir = os.path.dirname(os.path.realpath(__file__))
            data_dir = os.path.join(module_dir, '..', '..', 'data')
        
        src_font = os.path.join(data_dir, font_filename)
        if os.path.exists(src_font):
            shutil.copyfile(src_font, font_path)


def full_pixels(space, data, gap_pixels=1):
    """returns the given data distributed in the space ensuring it's full pixels
    and with the given gap.
    this will result in minor sub-pixel inaccuracies.
    """
    available = space - (len(data) - 1) * gap_pixels # 8 recs 7 gaps

    res = []
    for i, val in enumerate(data):
        # convert data to 0..1 scale so we deal with fractions
        data_sum = sum(data[i:])
        norm = val * 1.0 / data_sum


        w = max(int(round(available * norm)), 1)
        res.append(w)
        available -= w
    return res
