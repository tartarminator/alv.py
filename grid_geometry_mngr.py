# from tkinter import *
#
# root_window = Tk()
# root_window.title('Geometry')
# root_window.geometry()
#
# red_label = Label(root_window, text='Red', bg='red', fg='white', width=20, height=5)
# red_label.grid(row=0, column=0)
#
# yellow_label = Label(root_window, text='Yellow', bg='yellow', fg='red', width=20, height=5 )
# yellow_label.grid(row=0, column=1)
#
# green_label = Label(root_window, text='Green', bg='green', fg='white', width=20, height=5)
# green_label.grid(row=0, column=2)
#
# red_label_1 = Label(root_window, text='Red', bg='red', fg='white', width=20, height=5)
# red_label_1.grid(row=1, column=0)
#
# yellow_label_1 = Label(root_window, text='Yellow', bg='yellow', fg='red', width=20, height=5 )
# yellow_label_1.grid(row=1, column=1)
#
# green_label_1 = Label(root_window, text='Green', bg='green', fg='white', width=20, height=5)
# green_label_1.grid(row=1, column=2)
#
# button_1 = Button(root_window, text='Button 1', bg='brown')
# button_1.grid(row=2, column=0)
# button_2 = Button(root_window, text='Button 2', bg='blue')
# button_2.grid(row=2, column=1)
# button_3 = Button(root_window, text='Button 3', bg='salmon')
# button_3.grid(row=2, column=2)
#
#
# root_window.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Geometry Grid')

content = ttk.Frame(root, padding=(3, 3, 12, 12))
frame = ttk.Frame(content, borderwidth=20, relief="sunken", width=400, height=200)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar(value=True)
twovar = BooleanVar(value=False)
threevar = BooleanVar(value=True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()
