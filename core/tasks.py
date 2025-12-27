import json
from datetime import datetime
from core.state import AppState

def update_file(state: AppState) -> None:
    """Save the current program state to the JSON file."""
    with open("core/data.json", "w") as f:
        json.dump(state.data, f, indent=4)

def add_task(state: AppState, task_name: str) -> None:
   """Add a new task to the current level."""
   current_level = state.navigation[-1][1]
   now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   current_level.append({
        "name": task_name, 
        "description": "", 
        "date":now, 
        "subtasks":[]
   })
   update_file(state)

def remove_task(state: AppState, task_index: int) -> bool:
    """
    Remove a task at the given index from the current level.
    
    Returns True if the task was removed successfully, False if the index was invalid.
    """
    current_level = state.navigation[-1][1]
    if not current_level:
        return False
    
    if 0 <= task_index < len(current_level):
        current_level.pop(task_index)
        update_file(state)
        return True
    else:
        return False
    
def move_task(state: AppState, index: int, direction: str) -> bool:
    """
    Move a task at the given index up or down in the current level.

    direction: 'up' or 'down'
    Returns True if the move was successful, False if the move is invalid.
    """

    current_level = state.navigation[-1][1]

    if not current_level or not (0 <= index < len(current_level)):
        return False

    if direction == "up" and index > 0:
        current_level[index], current_level[index - 1] = current_level[index - 1], current_level[index]
        update_file(state)
        return True

    elif direction == "down" and index < len(current_level) - 1:
        current_level[index], current_level[index + 1] = current_level[index + 1], current_level[index]
        update_file(state)
        return True
    return False

def move_to_done(state: AppState, index: int) -> bool:
    """
    Move the task at the given index from the current level to the done list.

    Returns True if successful, False if the index is invalid or current level is empty.
    """
    current_level = state.navigation[-1][1]

    if not current_level or not (0 <= index < len(current_level)):
        return False

    state.done.append(current_level[index])
    current_level.pop(index)
    update_file(state)
    return True

def clear_done(state: AppState) -> bool:
    """
    Clear all tasks from the done list.

    Returns True if the done list was cleared, False if it was already empty.
    """
    if not state.done:
        return False
    state.done.clear()
    update_file(state) 
    return True

def get_path(state: AppState) -> str:
    """Return the current path as a string based on the navigation stack."""
    return "".join(level[0] for level in state.navigation)

def navigate_task(state: AppState, index: int | None = None) -> bool:
    """
    Navigate into a subtask or back.

    - If index is None, attempts to go back one level.
    - If index is an integer, navigates into that subtask.
    
    Returns True if navigation was successful, False if invalid.
    """
    if index is None:
        # Go back
        if len(state.navigation) > 1:
            state.navigation.pop()
            return True
        return False
    else:
        # Go into task
        current_level = state.navigation[-1][1]
        if 0 <= index < len(current_level):
            task = current_level[index]
            state.navigation.append((f"{task['name']}/", task["subtasks"]))
            return True
        return False
