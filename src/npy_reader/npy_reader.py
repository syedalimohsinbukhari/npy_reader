"""
Created on Feb 23 08:59:21 2022
"""

import PySimpleGUI as sg
import numpy as np


def main():
    filename = sg.popup_get_file(message='Browse to the .npy file you want to read!',
                                 title='.npy file reader',
                                 file_types=(('NumPy File', '.npy'),))

    fn = filename.split('/')[-1]
    _npy = np.load(fn, allow_pickle=True)

    heading_list = [f'V{i}' for i in range(len(_npy[0]))]

    layout = [[sg.Table(values=_npy.tolist(),
                        headings=heading_list,
                        auto_size_columns=True,
                        display_row_numbers=True,
                        num_rows=50)]]

    window = sg.Window(title=fn, layout=layout, resizable=True, auto_size_buttons=True, grab_anywhere=False, finalize=True)
    window.read()
    window.close()


if __name__ == '__main__':
    main()
