import tkinter
from tkinter import messagebox

my_window=tkinter.Tk()
my_window.title("ToDo List")
my_window.config(bg="#B692C2")
my_window.geometry("650x500+350+150")
my_window.resizable(False,False)


def add_task_listbox():
    task_text = task.get()
    if task_text:
        current_count = task_listbox.size() + 1
        task_listbox.insert(tkinter.END, f"{current_count}. {task_text}")
        task.delete(0, tkinter.END)
    messagebox.showinfo("Add","Task added successfully")

def delete_task_listbox():
    selected_index=task_listbox.curselection()
    if selected_index:
        task_listbox.delete(selected_index)
        update_task_numbers()
    messagebox.showinfo("Delete", "Task deleted successfully")

def update_task_numbers():
    items = task_listbox.get(0, tkinter.END)
    task_listbox.delete(0, tkinter.END)
    for i, item in enumerate(items, start=1):
        task_listbox.insert(tkinter.END, f"{i}. {item.split('. ', 1)[1]}")

def save_tasks():
    answer=messagebox.askyesno("Save","Do you want to save changes?")
    if answer:
        with open("my_todo_list.txt", "w", encoding="utf-8") as file:
            tasks = task_listbox.get(0, tkinter.END)
            for task in tasks:
                file.write(task + "\n")
        messagebox.showinfo("Save Successful", "Your changes were saved")
    else:
        messagebox.showinfo("Save Unsuccessful","Your changes were not saved")

def load_tasks():
    try:
        with open("my_todo_list.txt", "r", encoding="utf-8") as file:  # "r" ile dosyayı okuma modunda aç
            for line in file:
                task_listbox.insert(tkinter.END, line.strip())  # Her satırı Listbox'a ekle
    except FileNotFoundError:
        pass

my_window.after(100, load_tasks)


my_title=tkinter.Label(text="TO DO LIST",bg="#B692C2",font="Arial 30 italic bold")
my_title.place(x=220,y=0)

task=tkinter.Entry(width=70,bg="#E5D9F2",font="1")
task.focus()
task.place(x=0,y=90,height=40)

add_task=tkinter.Button(text="Add Task",bg="#9DBDFF",font="Arial 11 bold",command=add_task_listbox)
add_task.place(x=180,y=150)

clear_task=tkinter.Button(text="Delete Task",bg="#CB80AB",font="Arial 11 bold",command=delete_task_listbox)
clear_task.place(x=290,y=150)

save_task=tkinter.Button(text="Save Task",bg="#6482AD",font="Arial 11 bold",command=save_tasks)
save_task.place(x=420,y=150)

label2=tkinter.Label(text="TASKS",bg="#E5D9F2",font="Arial 13 italic bold underline")
label2.place(x=0,y=200)
task_listbox=tkinter.Listbox(width=70,height=12,bg="#E5D9F2",font="bold")
task_listbox.place(x=0,y=230)


my_window.mainloop()