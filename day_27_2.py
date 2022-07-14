from tkinter import *


def button_clicked():
    print(f"I got clicked")
    new_text = some_input.get()
    my_label.config(text=new_text)


# def spinbox_used():
#     print(spinbox.get())
#
#
# def scale_used(value):
#     print(value)
#
#
# def checkbutton_used():
#     print(checked_state.get())
#
#
# def radio_used():
#     print(radio_state.get())
#
#
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))


"""
tkinter ==> has three types of layout. i.e.:    1--> [pack] --> puts everything from top to bottom
                                                2--> [place]    --> puts at the place where it is designated but 
                                                                    you have to be very precise.
                                                3--> [grid] --> puts things in rows, columns.
                                                                it's the relative layout system.
WARNING: you cannot mix and match .grid() and .pack() together in same app.
"""


window = Tk()
window.title("My first GUI program.")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

# ---------- label ----------
my_label = Label(text="I am some label.", font=("Arial", 18, "bold"))
my_label.config(text="new text")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.config(padx=30, pady=30)
my_label.grid(column=0, row=0)

# ---------- Button ----------
button = Button(text="Click Me!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button_2 = Button(text="Don't Click Me!", command=button_clicked)
button_2.grid(column=2, row=0)

# ---------- Entry ----------
some_input = Entry(width=40)
some_input.insert(END, string="Some text to begin with.")
print(some_input.get())
# some_input.pack()
some_input.grid(column=3, row=3)
# # ---------- Text ----------
# text = Text(height=5, width=30)
# text.focus()
# text.insert(END, "Example of multi-line text entry.")
# print(text.get("1.0", END))
# text.pack()
#
# # ---------- Spinbox ----------
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# # ---------- Scale ----------
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# # ---------- Checkbutton ----------
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# # ---------- Radiobutton ----------
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
# # ---------- Listbox ----------
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

window.mainloop()
