import tkinter

root = tkinter.Tk()

def event():
    label2 = tkinter.Label(root, text = "button pushed")
    label2.pack()

label = tkinter.Label(root, text = "halo ini adalah GUI\n menggunakan tkinter")
tombol = tkinter.Button(root, text = "push me", command = event)

label.pack()
tombol.pack()
root.mainloop()