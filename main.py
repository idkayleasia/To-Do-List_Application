# To Do list Application
# By @idkayleasia
# To-Do list contains listbox, scroll bar (both listbox and scroll bar inside frame), entry widget, buttons ( add, remove, save, load)

import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("To Do List by @idkayleasia")


def addTask():
    task = entryTask.get()
    if task != "":
        listBox.insert(tkinter.END, task)
        entryTask.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


def removeTask():
    try:
        selectedTaskIndex = listBox.curselection()[0]
        listBox.delete(selectedTaskIndex)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task to remove")


def saveTask():
    global savedTasks
    savedTasks = listBox.get(0, tkinter.END)
    if savedTasks:
        tkinter.messagebox.showinfo(title="Success", message="Tasks saved successfully.")
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="No tasks to save.")



def loadTask():
    if savedTasks:
        listBox.delete(0, tkinter.END)  # Clear the current tasks in the listbox
        for task in savedTasks:
            listBox.insert(tkinter.END, task)
        tkinter.messagebox.showinfo(title="Success", message="Tasks loaded successfully.")
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="No saved tasks to load.")

# GUI

frameTasks = tkinter.Frame(root)
frameTasks.pack()

listBox = tkinter.Listbox(frameTasks, height=10, width=80)
listBox.pack(side=tkinter.LEFT)

scrollBarTasks = tkinter.Scrollbar(frameTasks)
scrollBarTasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listBox.config(yscrollcommand=scrollBarTasks.set)
scrollBarTasks.config(command=listBox.yview)

entryTask = tkinter.Entry(root, width=80)
entryTask.pack()

addTaskButton = tkinter.Button(root, text="Add Task", width=70, command=addTask)
addTaskButton.pack()

removeTaskButton = tkinter.Button(root, text="Delete Task", width=70, command=removeTask)
removeTaskButton.pack()

saveTaskButton = tkinter.Button(root, text="Save Task(s)", width=70, command=saveTask)
saveTaskButton.pack()

loadTaskButton = tkinter.Button(root, text="Load Task(s)", width=70, command=loadTask)
loadTaskButton.pack()

root.mainloop()
