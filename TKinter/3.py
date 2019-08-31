import tkinter as tk
import time

class A:
    def __init__(self, master):
        self.label=tk.Label(master)
        self.label.grid(row=0, column=0)
        self.label.configure(text='nothing')
        self.root = root.geometry("800x800"),root.resizable(width=False,height=False)
        self.count = 0
        self.update_label()

    def update_label(self):
        if self.count < 10:
            self.label.configure(text = 'count: {}'.format(self.count))
            self.label.after(1000, self.update_label)
            self.count += 1
        print(self.count)





root = tk.Tk()
A(root)
root.mainloop()