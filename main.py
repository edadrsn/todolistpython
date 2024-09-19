import tkinter
from tkinter import messagebox

my_window=tkinter.Tk()
my_window.title("ToDo List")
my_window.config(bg="#B692C2")
my_window.geometry("650x510+350+150")
my_window.resizable(False,False)


def add_task_listbox():
    task_text = task.get()
    if task_text:
        current_count = task_listbox.size() + 1
        task_listbox.insert(tkinter.END, f"{current_count}. {task_text}")
        task.delete(0, tkinter.END)
    messagebox.showinfo("Add","Task added successfully")


deleted_tasks = []
def delete_task_listbox():
    selected_index = task_listbox.curselection()
    answer = messagebox.askyesno("Question", "Are you sure you want to delete the task?")

    if answer:
        if selected_index:
            task = task_listbox.get(selected_index)
            task_listbox.delete(selected_index)
            update_task_numbers()
            deleted_tasks.append(task)
            messagebox.showinfo("Info", "Task deleted successfully")
    else:
        messagebox.showinfo("Info", "Task not deleted")


def show_delete_list():
    toplevel = tkinter.Toplevel()
    toplevel.title("Deleted Tasks")
    toplevel.config(bg="#CDC1FF")
    toplevel.geometry("400x300+500+250")

    if deleted_tasks:
        deleted_tasks_listbox = tkinter.Listbox(toplevel, height=10, width=50,bg="#CDC1FF",font="bold 10")
        deleted_tasks_listbox.pack()

        for task in deleted_tasks:
            deleted_tasks_listbox.insert(tkinter.END, task)
    else:
        no_task_label = tkinter.Label(toplevel, text="NO DELETED TASK",font="Arial 10 bold ",bg="#CDC1FF")
        no_task_label.pack()

    close_button = tkinter.Button(toplevel, text="Close Window", fg="#F5F5F5", bg="#8967B3",font="Arial 12 italic bold", command=toplevel.destroy)
    close_button.place(x=150, y=250)
    toplevel.mainloop()


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
add_task.place(x=120,y=150)

clear_task=tkinter.Button(text="Delete Task",bg="#CB80AB",font="Arial 11 bold",command=delete_task_listbox)
clear_task.place(x=220,y=150)

save_task=tkinter.Button(text="Save Task",bg="#6482AD",font="Arial 11 bold",command=save_tasks)
save_task.place(x=340,y=150)

bin_button=tkinter.Button(text="Show Bin",bg="#CDC1FF",font="Arial 11 bold",command=show_delete_list)
bin_button.place(x=445,y=150)

label2=tkinter.Label(text="TASKS",bg="#E5D9F2",font="Arial 13 italic bold underline")
label2.place(x=0,y=200)
task_listbox=tkinter.Listbox(width=70,height=12,bg="#E5D9F2",font="bold")
task_listbox.place(x=0,y=230)

close_window=tkinter.Button(text="Exit Todo",bg="#2E073F",fg="#FFFFFF",font="Arial 12 bold",command=my_window.destroy)
close_window.place(x=250,y=470)

my_window.mainloop()