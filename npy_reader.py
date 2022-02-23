"""
Created on Feb 23 08:59:21 2022
"""

import tkinter as tk

###################################################################################
# Initialization
###################################################################################

# dimensions of the GUI window
from tkinter import filedialog

_w, _h = 250, 100
# main is the master name in which all work is going to be done
main = tk.Tk()
# set the title of the GUI window
main.title('NPY file reader')
# set the size of the GUI window
main.geometry(f'{_w}x{_h}')

# do not let the window be resized
main.resizable(False, False)


###################################################################################
# Functions
###################################################################################

def open_file_dialog_box():
    path = filedialog.askopenfile(initialdir='.', title='Select .npy file',
                                  filetypes=(('npy files', '*.npy'), ("all files", "*.*")))


###################################################################################
# TK_working
###################################################################################

label_file = tk.Label(master=main, text='Browse npy files: ')
label_file.place(x=_w / 2, y=20, anchor=tk.CENTER)

open_button = tk.Button(master=main, text='Open dialog box', command=open_file_dialog_box)
open_button.place(x=_w / 2, y=60, anchor=tk.CENTER)

main.mainloop()
