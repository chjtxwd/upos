import tkinter as tk
import subprocess

class APP:

    def __init__(self, master):  # root 传参赋值给master

        frame = tk.Frame(master)  # frame 组件

        frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.hi_there = tk.Button(frame, text='Restart RFID', bg='black', fg='white',
                                  command=self.restartrfid)  # Button按钮, command中调用定义的方法

        self.hi_there.pack()

    def restartrfid(self):
        subprocess.Popen('c:\\temp\\a.bat', creationflags=subprocess.CREATE_NEW_CONSOLE)


root = tk.Tk()
root.title("")
root.geometry("200x200")
root.resizable(0,0)
root.columnconfigure(0, weight=1)
app = APP(root)
root.mainloop()
