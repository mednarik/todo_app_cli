from core.tasks import add_task, remove_task, move_task, get_path, navigate_task, move_to_done, clear_done
import tkinter as tk

def add_task_gui(state):
    pass
def remove_task_gui(state):
    pass
def move_task_gui(state):
    pass
def navigate_task_gui(state):
    pass
def move_to_done_gui(state):
    pass

def run_gui(state):
    window = tk.Tk()
    window.geometry("600x600")

    #----------------- All Top Buttons -------------------
    top_buttons = tk.Frame(window)
    top_buttons.pack(side="top", fill="x")

    add_task_button = tk.Button(top_buttons, text="Add", command=lambda: add_task_gui(state))
    add_task_button.grid(row=0, column=0, sticky="ew")
    top_buttons.columnconfigure(0, weight=1)

    remove_task_button = tk.Button(top_buttons, text="Remove", command=lambda: remove_task_gui(state))
    remove_task_button.grid(row=0, column=1, sticky="ew")
    top_buttons.columnconfigure(1, weight=1)

    quit_button = tk.Button(top_buttons, text="Quit", command=window.destroy)
    quit_button.grid(row=0, column=2, sticky="ew")
    top_buttons.columnconfigure(2, weight=1)

    reorder_button = tk.Button(top_buttons, text="Reorder", command=lambda: move_task_gui(state))
    reorder_button.grid(row=0, column=3, sticky="ew")
    top_buttons.columnconfigure(3, weight=1)

    navigate_task_button = tk.Button(top_buttons, text="Navigate", command=lambda: navigate_task_gui(state))
    navigate_task_button.grid(row=0, column=4, sticky="ew")
    top_buttons.columnconfigure(4, weight=1)

    move_done_button = tk.Button(top_buttons, text="Complete", command=lambda: move_to_done_gui(state))
    move_done_button.grid(row=0, column=5, sticky="ew")
    top_buttons.columnconfigure(5, weight=1)

    clear_done_button = tk.Button(top_buttons, text="Clear Done", command=lambda: clear_done(state))
    clear_done_button.grid(row=0, column=6, sticky="ew")
    top_buttons.columnconfigure(6, weight=1)


    

    window.mainloop()
