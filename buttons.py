#!/usr/bin/env python3
import backend
import subprocess
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

s = subprocess.getstatusoutput('sudo pigpiod')
if s[0] == 0:
    print(s[1])
else:
    print('Error {}'.format(s[1]))

# left = backend.Drawer_Servo(13)
right = backend.Drawer_Servo(12)

ttk.Label(frm, text="Drawer Control").grid(column=50, row=0)
ttk.Button(frm, text="Right Drawer", command=right.toggle_drawer()).grid(column=45, row=20, padx=5, pady=20) #command=right.toggle_drawer)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=50, row=30, padx=20, pady=20)
root.mainloop()