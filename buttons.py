#!/usr/bin/env python3
import subprocess
commands = [
        ["source env/bin/activate"], # enter the right environment first
        ["sudo pigpiod"]
    ]

for cmd in commands:
    result = subprocess.run(cmd, check=True, text=True, capture_output=True)
    print(result.stdout)

from backend import Drawer_Servo
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

servo_hat = Drawer_Servo()

ttk.Label(frm, text="Drawer Control").grid(column=50, row=0)
ttk.Button(frm, text="Right Drawer", command=servo_hat.toggle_drawer(0)).grid(column=45, row=20, padx=5, pady=20) #command=right.toggle_drawer)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=50, row=30, padx=20, pady=20)
root.mainloop()