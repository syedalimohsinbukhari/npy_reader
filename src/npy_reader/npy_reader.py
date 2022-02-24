"""
Created on Feb 23 08:59:21 2022
"""

import tkinter as tk

from functions import hide_show_hidden_files, open_file_dialog_box

###################################################################################
# Initialization
###################################################################################

# set the width and height of the original window
_w, _h = 250, 100
# main is the master name in which all work is going to be done
main = tk.Tk()
# set the title of the GUI window
main.title('NPY file reader')
# set the size of the GUI window
main.geometry(f'{_w}x{_h}')

# do not let the window be resized
main.resizable(False, False)

# also do not let it be resized smaller than it already is
main.minsize(_w, _h)

hide_show_hidden_files(main)

###################################################################################
# TK_decorations
###################################################################################

label_file = tk.Label(master=main, text='Browse npy files: ')
label_file.place(x=_w / 2, y=20, anchor=tk.CENTER)

# command/lambda taken from https://stackoverflow.com/a/6921225/3212945
open_button = tk.Button(master=main, text='Open dialog box', command=lambda: open_file_dialog_box(windows=main))
open_button.place(x=_w / 2, y=60, anchor=tk.CENTER)

main.mainloop()
