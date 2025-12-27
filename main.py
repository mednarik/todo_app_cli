import json
from core.state import AppState
from ui.cli import run_cli

def main():
    with open("core/data.json", "r") as f:
        data = json.load(f)

    state = AppState(data)
    run_cli(state)

if __name__ == "__main__":
    main()