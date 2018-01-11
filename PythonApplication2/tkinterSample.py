import tkinter

root = tkinter.Tk()

# title bar
root.title("MyGUIApp")
root.geometry("300x200") # px

btn = tkinter.Button(root, text="click", width="5")
lbl = tkinter.Label(root, text="xxxxxxxxxxx", foreground="#ff0000", background="#0000ff")
edt = tkinter.Entry(root, width="5")
valB = tkinter.BooleanVar()
valB.set(True)
chk = tkinter.Checkbutton(root, text="check", variable=valB)
valI = tkinter.IntVar()
valI.set(0)

rdo1 = tkinter.Radiobutton(root, text="item1", variable=valI, value = 0)
rdo2 = tkinter.Radiobutton(root, text="item2", variable=valI, value = 1)
rdo3 = tkinter.Radiobutton(root, text="item3", variable=valI, value = 2)

btn.place(x = 100, y = 100);
lbl.grid(row = 0, column = 0)
edt.grid(row = 1, column = 0)
chk.grid(row = 1, column = 1)

root.mainloop()
