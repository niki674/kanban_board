import tkinter


def create_task():
    global entry
    task = entry.get()
    if  task:
        to_do_list.insert(tkinter.END, task)
        entry.delete(0, tkinter.END)


def move_task(souce_list, target_list):
    task = souce_list.get(souce_list.curselection())
    if  task:
        target_list.insert(tkinter.END, task)
        souce_list.delete(souce_list.curselection())


window = tkinter.Tk()
window.title('Kanban Board')

to_do_list = tkinter.Listbox(window, height=25, width=30)
in_progress_list = tkinter.Listbox(window, height=25, width=30)
completed_list = tkinter.Listbox(window, height=25, width=30)

to_do_list.grid(row=0, column=0, padx=10, pady=10)
in_progress_list.grid(row=0, column=1, padx=10, pady=10)
completed_list.grid(row=0, column=2, padx=10, pady=10)

to_do_list.bind('<Double-Button-1>', lambda e: move_task(to_do_list, in_progress_list))
in_progress_list.bind('<Double-Button-1>', lambda e: move_task(in_progress_list, completed_list))
completed_list.bind('<Double-Button-1>', lambda e: completed_list.delete(completed_list.curselection()))

add_label = tkinter.Label(window, text='Add task: ')
add_label.grid(row=1, column=0, pady=5)

entry = tkinter.Entry(window, width=30)
entry.grid(row=1, column=1, pady=5)

add_button = tkinter.Button(
    text='Add',
    command= create_task,
    )
add_button.grid(row=1, column=2, pady=5)

delete_button = tkinter.Button(
    text='Del all tasks',
    command= lambda: (to_do_list.delete(0, tkinter.END), in_progress_list.delete(0, tkinter.END), completed_list.delete(0, tkinter.END))
    )
delete_button.grid(row=2, column=2, pady=5)

window.mainloop()
