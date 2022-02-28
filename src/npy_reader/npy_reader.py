"""
Created on Feb 23 08:59:21 2022
"""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import numpy as np


def main():
    ###################################################################################
    # Functions
    ###################################################################################

    def hide_show_hidden_files(main_window):
        # originally posted, https://code.activestate.com/lists/python-tkinter-discuss/3723
        # taken from, https://stackoverflow.com/a/54068050/3212945
        try:
            main_window.tk.call('tk_getOpenFile', '-foobarbaz')
        except tk.TclError:
            pass

        main_window.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
        main_window.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')

    def display_npy_file(npy_file, windows):
        # convert the array to list so each value is comma separated
        n_npy = [list(i) for i in npy_file]

        # define a new window
        new_window = tk.Toplevel(windows)
        new_window.title('NPY file')

        # get the screen information
        _f_w, _f_h = new_window.winfo_screenwidth(), new_window.winfo_screenheight()

        # set the new window size to half of the screen (just because)
        new_window.geometry(f'{int(_f_w / 2)}x{int(_f_h / 2)}')

        # don't let the window be resized smaller than quarter of the screen size (just because)
        new_window.minsize(int(_f_w / 4), int(_f_h / 4))

        # make a new frame within the new window,
        # frame is like a container which will hold all other widgets in it
        frame = tk.Frame(new_window, width=_f_w)
        frame.pack()

        # define the horizontal and vertical scrollbars
        scrollbar_x = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
        scrollbar_y = tk.Scrollbar(frame, orient=tk.VERTICAL)

        # since we're trying to read a npy file, which comes without the information of header
        # we will use the R-Studio method, by naming every column as V[column-number]
        # as in, the first column would be labelled as V0, then V1, and so on.
        # for that we require the length of the first element of our npy_file, as the npy file
        # always has the same number of columns
        cols = [f'V{i}' for i in range(len(n_npy[0]))]

        # this is where we will display the contents in tabular form
        # as we're making the Treeview widget inside the "frame" we need only to specify the height,
        # the width will be of the "frame" itself
        tree_view = ttk.Treeview(frame,
                                 columns=cols,
                                 height=_f_h,
                                 selectmode='extended',
                                 yscrollcommand=scrollbar_y.set,
                                 xscrollcommand=scrollbar_x.set)

        # configure the x-scrollbar
        scrollbar_x.config(command=tree_view.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # configure the y-scrollbar
        scrollbar_y.config(command=tree_view.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        # insert headings into the tree_view,
        # headings will introduce the variable names on the top, V0, V1, V2, .. etc
        [tree_view.heading(f'V{i}', text=f'V{i}', anchor=tk.W) for i in range(len(npy_file[0]))]

        # set the minimum and maximum allowed width for the columns
        [tree_view.column(f'#{i}', minwidth=100, width=150) for i in range(len(npy_file[0]))]

        # insert the values in the viewer
        [tree_view.insert('', 0, values=i) for i in n_npy]

        # pack it up :)
        tree_view.pack()

    def open_file_dialog_box(windows):
        try:
            npy_file = filedialog.askopenfile(initialdir=os.environ['PWD'], title='Select .npy file', filetypes=([('npy files', '*.npy')]))
            npy_file = np.load(npy_file.name, allow_pickle=True)
            display_npy_file(npy_file, windows)
        except AttributeError:
            # if no file is selected/Cancel is pressed, alert the user,
            # don't throw exception
            messagebox.showinfo(title='No npy file selected', message='Please select a .npy file.')

    ###################################################################################
    # Initialization
    ###################################################################################

    # set the width and height of the original window
    _w, _h = 250, 100
    # main is the master name in which all work is going to be done
    root_window = tk.Tk()
    # set the title of the GUI window
    root_window.title('NPY file reader')
    # set the size of the GUI window
    root_window.geometry(f'{_w}x{_h}')

    # do not let the window be resized
    root_window.resizable(False, False)

    # also do not let it be resized smaller than it already is
    root_window.minsize(_w, _h)

    hide_show_hidden_files(root_window)

    ###################################################################################
    # TK_decorations
    ###################################################################################

    label_file = tk.Label(master=root_window, text='Browse npy files: ')
    label_file.place(x=_w / 2, y=20, anchor=tk.CENTER)

    # command/lambda taken from https://stackoverflow.com/a/6921225/3212945
    open_button = tk.Button(master=root_window, text='Open dialog box', command=lambda: open_file_dialog_box(windows=root_window))
    open_button.place(x=_w / 2, y=60, anchor=tk.CENTER)

    root_window.mainloop()


###################################################################################
# run
###################################################################################

# taken from https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
if __name__ == '__main__':
    try:
        sys.exit(main())
    except TypeError:
        pass
