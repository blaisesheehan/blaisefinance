import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Finance Tracker")

ttl_frm =  tk.Frame(root)
ttl_frm.pack(side=tk.TOP, padx=10, pady=90)

ttl = tk.Label(ttl_frm, text = "Blaise's Finance Tracker", font = ("Helvetica", 40))
ttl.pack()

button_frm = tk.Frame(root)
button_frm.pack(side=tk.LEFT, padx=10, pady=10)

add = ttk.Button(button_frm, text="Add")
delete = ttk.Button(button_frm, text="Delete")
edit = ttk.Button(button_frm, text="Edit")


add.pack(fill =tk.X, padx=10, pady=5)
delete.pack(fill=tk.X, padx=10, pady=5)
edit.pack(fill=tk.X, padx=10, pady=5)

tbl_frm = tk.Frame(root)
tbl_frm.pack(side=tk.RIGHT, padx=10, pady=10)

tbl_lbl = ttk.Label(tbl_frm, text="LOGIC OF EXPENSES")
tbl_lbl.pack()

root.mainloop()
