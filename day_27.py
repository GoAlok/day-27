from tkinter import *

window = Tk()
window.title("My first GUI program.")
window.minsize(width=600, height=600)

# ---------- label ----------
my_label = Label(text="I am some label.", font=("Arial", 18, "bold"))
my_label.pack()  # component_name.pack() --> It let component show on the screen. Must be needed to shown on screen
# my_label.pack(expand=True)
# my_label.pack(side='left')
my_label["text"] = "new text"  # <--


# ---OR----
# my_label.config(text="new text")  # <--


# ---------- Button ----------
def button_clicked():
    print(f"I got clicked")
    new_text = some_input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me!", command=button_clicked)
button.pack()

# ---------- Entry ----------
some_input = Entry(width=40)
# Adds some text to begin with.
some_input.insert(END, string="Some text to begin with.")
print(some_input.get())  # Gets text in entry
some_input.pack()

# ---------- Text ----------
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))  # "1.0" means starting from 1st line and form 1st character
text.pack()


# ---------- Spinbox ----------
def spinbox_used():
    # gets current value of spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# ---------- Scale ----------
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# ---------- Checkbutton ----------
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# ---------- Radiobutton ----------
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# ---------- Listbox ----------
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
