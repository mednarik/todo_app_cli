# ui/cli.py
from core.tasks import add_task, remove_task, move_task, get_path, navigate_task, move_to_done, clear_done
import os

# Terminal styling
UNDERLINE_BOLD = "\033[1;4m"
RESET = "\033[0m"

def clear_screen() -> None:
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def get_proper_index(index_str: str) -> int | None:
    """Convert user input to zero-based index. Returns None if invalid."""
    try:
        return int(index_str) - 1
    except ValueError:
        return None

def show_tasks(state) -> str:
    """Return a string showing current tasks and done list."""
    current_level = state.navigation[-1][1]
    done_list = state.done
    max_rows = max(len(current_level), len(done_list))
    tab = 50

    lines = [f"{UNDERLINE_BOLD}Path{RESET}: {get_path(state)}", ""]
    lines.append(f"{UNDERLINE_BOLD}{'To Do':<{tab}}|{'Done':<{tab}}{RESET}")

    for i in range(max_rows):
        todo_text = f"{i+1}. {current_level[i]['name']}" if i < len(current_level) else ""
        done_text = done_list[i]['name'] if i < len(done_list) else ""
        lines.append(f"{todo_text:<{tab}}|{done_text}")

    return "\n".join(lines)

# ---------- CLI wrappers for core logic ----------

def add_task_cli(state):
    task_name = input("New task name: ").strip()
    if task_name:
        add_task(state, task_name)
        print("Task added!")
    else:
        print("Task name cannot be empty.")
    input("Press Enter to continue...")

def remove_task_cli(state):
    print(show_tasks(state))
    index_str = input("Enter the index of the task to remove: ")
    idx = get_proper_index(index_str)
    if idx is not None and remove_task(state, idx):
        print("Task removed!")
    else:
        print("Invalid index.")
    input("Press Enter to continue...")

def move_task_cli(state):
    print(show_tasks(state))
    index_str = input("Enter the index of the task to move: ")
    idx = get_proper_index(index_str)
    if idx is None:
        print("Invalid index.")
        input("Press Enter to continue...")
        return

    direction = input("Move 'up' or 'down'? ").strip().lower()
    if direction in ("up", "down") and move_task(state, idx, direction):
        print("Task moved!")
    else:
        print("Invalid move.")
    input("Press Enter to continue...")

def navigate_task_cli(state):
    print(show_tasks(state))
    choice = input("Enter task index to open, or 'a' to go back: ").strip().lower()
    if choice == 'a':
        if navigate_task(state):
            print("Moved up one level.")
        else:
            print("Already at root level.")
    else:
        idx = get_proper_index(choice)
        if idx is not None and navigate_task(state, idx):
            print("Entered subtask.")
        else:
            print("Invalid index.")
    input("Press Enter to continue...")

def move_to_done_cli(state):
    print(show_tasks(state))
    index_str = input("Enter the index of the completed task: ")
    idx = get_proper_index(index_str)
    if idx is not None and move_to_done(state, idx):
        print("Task moved to Done.")
    else:
        print("Invalid index.")
    input("Press Enter to continue...")

def clear_done_cli(state):
    if clear_done(state):
        print("Done list cleared.")
    else:
        print("Done list is already empty.")
    input("Press Enter to continue...")

# ---------- Main CLI loop ----------

def run_cli(state):
    while True:
        clear_screen()
        print(show_tasks(state))
        print(f"\n{UNDERLINE_BOLD}Controls{RESET}")
        print("1: Add task")
        print("2: Remove task")
        print("3: Quit")
        print("4: Change task order")
        print("5: Open a task")
        print("6: Move task from To Do to Done")
        print("7: Clear Done list")
        
        action = input(">>> ").strip()

        clear_screen()

        if action == "1":
            add_task_cli(state)
        elif action == "2":
            remove_task_cli(state)
        elif action == "3":
            break
        elif action == "4":
            move_task_cli(state)
        elif action == "5":
            navigate_task_cli(state)
        elif action == "6":
            move_to_done_cli(state)
        elif action == "7":
            clear_done_cli(state)
        else:
            input("Not a valid action. Press Enter to continue...")
