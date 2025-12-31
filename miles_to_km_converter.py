from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=90, height=90)
window.config(padx=30, pady=25)

#def_calculate
def converter():
    miles = float(user_input.get())
    km = miles*1.6
    user_input_2.config(text=km)





#entry
user_input = Entry()
user_input.grid(row=0, column=2)
user_input.config(width=8)
user_input.insert(END, string="0")

#text
text = Label(text="Miles")
text.grid(row=0, column=3)

#second entry !!!! it's not entry, it should be text....

user_input_2 = Label(text="0") #==>> instead of miles need variable
user_input_2.grid(row=1, column=2)
user_input_2.config(width=8)

#second text
text_2 = Label(text="Km")
text_2.grid(row=1, column=3)

#text-3
text_3 = Label(text="is equal to")
text_3.grid(row=1, column=1)

#button
button = Button(text="Calculate", command=converter)
button.grid(row=2, column=2)


window.mainloop()
