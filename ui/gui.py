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

def show_top_container(state, window):
    # Parent container for toolbar + path
    top_container = tk.Frame(window)
    top_container.place(relx=0, rely=0, relwidth=1, relheight=0.25)

    sticky = "nsew"
    font = ("TkDefaultFont", 15)

    # Toolbar frame inside top_container
    top_buttons = tk.Frame(top_container)
    top_buttons.pack(side="top", fill="both", expand=True)
    top_buttons.rowconfigure(0, weight=1)

    # Add buttons manually, no padding
    add_task_button = tk.Button(top_buttons, text="Add", command=lambda: add_task_gui(state), font=font)
    add_task_button.grid(row=0, column=0, sticky=sticky)
    top_buttons.columnconfigure(0, weight=1)

    remove_task_button = tk.Button(top_buttons, text="Remove", command=lambda: remove_task_gui(state), font=font)
    remove_task_button.grid(row=0, column=1, sticky=sticky)
    top_buttons.columnconfigure(1, weight=1)

    quit_button = tk.Button(top_buttons, text="Quit", command=window.destroy, font=font)
    quit_button.grid(row=0, column=2, sticky=sticky)
    top_buttons.columnconfigure(2, weight=1)

    reorder_button = tk.Button(top_buttons, text="Reorder", command=lambda: move_task_gui(state), font=font)
    reorder_button.grid(row=0, column=3, sticky=sticky)
    top_buttons.columnconfigure(3, weight=1)

    navigate_task_button = tk.Button(top_buttons, text="Navigate", command=lambda: navigate_task_gui(state), font=font)
    navigate_task_button.grid(row=0, column=4, sticky=sticky)
    top_buttons.columnconfigure(4, weight=1)

    move_done_button = tk.Button(top_buttons, text="Complete", command=lambda: move_to_done_gui(state), font=font)
    move_done_button.grid(row=0, column=5, sticky=sticky)
    top_buttons.columnconfigure(5, weight=1)

    clear_done_button = tk.Button(top_buttons, text="Clear Done", command=lambda: clear_done(state), font=font)
    clear_done_button.grid(row=0, column=6, sticky=sticky)
    top_buttons.columnconfigure(6, weight=1)

    # Path label directly below toolbar
    path_label = tk.Label(top_container, text=get_path(state), font=font)
    path_label.pack(side="top", fill="x")

def run_gui(state):
    window = tk.Tk()
    window.geometry("600x600")

    #----------------- All Top Buttons + Path -------------------
    show_top_container(state, window)

    # Bottom content frame for the rest of the window
    content_frame = tk.Frame(window, bg="white")
    content_frame.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

    window.mainloop()
