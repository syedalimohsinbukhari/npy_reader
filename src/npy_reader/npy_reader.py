"""
Created on Feb 23 08:59:21 2022
"""

import os
import sys

import numpy as np
import PySimpleGUI as pySG


def npy_reader():
    """
    Main function to read the npy files.
    """
    # Get the file to read from the user
    filename = pySG.popup_get_file(message='Browse to the .npy file you want to read!', title='.npy file reader',
                                   file_types=(('NumPy File', '.npy'),))

    # Get the file name from the file path
    fn = os.path.basename(filename)

    # Load the NumPy array from the file,
    # memory mapping it to allow access to the data without reading it all into memory
    _npy = np.load(filename, allow_pickle=True, mmap_mode='r')
    # Generate a list of headings for the table
    heading_list = [f'V{i}' for i in range(len(_npy[0]))]

    # Create the layout for the window
    layout = [[pySG.Table(values=_npy.tolist(), headings=heading_list, auto_size_columns=True, display_row_numbers=True,
                          num_rows=50, pad=5, expand_x=True, expand_y=True)]]

    # Create the window and display it to the user
    window = pySG.Window(size=(1000, 600), title=fn, layout=layout, resizable=True, auto_size_buttons=True,
                         grab_anywhere=False)
    window.read()
    window.close()


def main():
    try:
        npy_reader()
    except TypeError:
        pass


if __name__ == '__main__':
    try:
        sys.exit(main())
    except TypeError:
        pass
