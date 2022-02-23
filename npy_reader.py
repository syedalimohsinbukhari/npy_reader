"""
Created on Feb 23 08:59:21 2022
"""

import tkinter as tk

# dimensions of the GUI window
_w, _h = 280, 140
# main is the master name in which all work is going to be done
main = tk.Tk()
# set the title of the GUI window
main.title('NPY file reader')
# set the size of the GUI window
main.geometry(f'{_w}x{_h}')

main.mainloop()
