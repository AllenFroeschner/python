import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps=tempApps.split(',')
        apps= [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/", title="select file",
                                          filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#C62488")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=.8, relheight=.8, relx=.1, rely=.1)

OpenFile = tk.Button(root, text="open file", padx=10, pady=5,
                     fg="white", bg="#C62488", command=addApp)
OpenFile.pack()

RunApps = tk.Button(root, text="Run App", padx=10, pady=5,
                     fg="white", bg="#C62488", command=runApps)
RunApps.pack()

for app in apps:
    label =tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open ('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')