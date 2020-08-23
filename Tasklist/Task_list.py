from tkinter import *
from db import Database
from tkinter import messagebox
from time import strftime
import datetime as dt

db = Database('mytask.db')

def populate_list():
    my_list.delete(0, END)
    for record in db.fetch():
        my_list.insert(END, record)


def add_task():
    if my_text.get() == '':
        messagebox.showerror('Enter task', 'Please enter task')
        return
    db.insert(my_text.get())
    my_list.delete(0, END)
    my_list.insert(END, (my_text.get()))
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = my_list.curselection()[0]
        selected_item = my_list.get(index)

        task_entry.delete(0, END)
        task_entry.insert(END, selected_item[1])

    except IndexError:
        pass


def remove_task():
    db.remove(selected_item[0])
    populate_list()


def removeall_task():
    db.removeall()
    populate_list()


def update_task():
    db.update(selected_item[0], my_text.get())
    populate_list()


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


app = Tk()

# My tasks

my_label = Label(app, text='Enter task below', font=('calibri,14', 11, 'bold'), border=0, fg='black',
                 bg='lightsteelblue4', )
my_label.place(x=125, y=0)

my_text = StringVar()
task_entry = Entry(app, textvariable=my_text, font=('calibri', 11, 'bold'), border=0, fg='black', bg='lightsteelblue1',
                   width=30)
task_entry.place(x=81, y=20)

# Task List (Listbox)

my_list = Listbox(app, height=12, width=30, font=('calibri', 11, 'bold'), border=0, fg='black', bg='lightsteelblue1')
my_list.place(x=81, y=41)

# Scrollbar

scrollbar = Scrollbar(app)
scrollbar.place(x=292, y=0, height=270)

# Scrollbar to listbox
my_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=my_list.yview)

# Bind select
my_list.bind('<<ListboxSelect>>', select_item)

# Buttons

add_btn = Button(app, text='Add task', font=('calibri', 10, 'bold'), bg='lightsteelblue4', fg='lightsteelblue1',
                 width=10, height=4, command=add_task)
add_btn.place(x=0, y=0)

remove_btn = Button(app, text='Remove task', font=('calibri', 10, 'bold'), bg='lightsteelblue4', fg='lightsteelblue1',
                    width=10, height=4, command=remove_task)
remove_btn.place(x=0, y=140)

removeall_btn = Button(app, text='Remove all', font=('calibri', 10, 'bold'), bg='lightsteelblue4', fg='lightsteelblue1',
                       width=10, height=4, command=removeall_task)
removeall_btn.place(x=0, y=211)

update_btn = Button(app, text='Update task', font=('calibri', 10, 'bold'), bg='lightsteelblue4', fg='lightsteelblue1',
                    width=10, height=4, command=update_task)
update_btn.place(x=0, y=71)

exit = Button(app, text='Exit', font=('calibri', 10, 'bold'), width=10, height=4, bg='lightsteelblue4',
              fg='lightsteelblue1', command=exit)
exit.place(x=0, y=282)

lbl = Label(app, font=('calibri', 33, 'bold'), border=0, bg='lightsteelblue4', fg='black')
lbl.place(x=80, y=287)
time()

app.title('Task manager')
app.geometry('310x353')
app.configure(bg='lightsteelblue4')
app.iconbitmap('C:/Users/Henri/Downloads/photo.ico')

# Populate data

populate_list()

# Main Loop
app.mainloop()
