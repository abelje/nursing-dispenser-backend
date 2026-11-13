#!/usr/bin/env python3
import subprocess
import drawer
from tkinter import *
from tkinter import ttk

drawer.init_hat()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Drawer Control").grid(column=50, row=0)
ttk.Button(frm, text="Right Drawer", command=lambda: drawer.open_drawer(0)).grid(column=45, row=20, padx=5, pady=20) #command=right.toggle_drawer)
ttk.Button(frm, text="Right Drawer", command=lambda: drawer.open_drawer(1)).grid(column=55, row=20, padx=5, pady=20)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=50, row=30, padx=20, pady=20)
root.mainloop()