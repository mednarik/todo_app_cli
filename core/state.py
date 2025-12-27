class AppState:
    def __init__(self, data: dict):
        self.data = data
        self.done = data["done"]
        self.navigation = [("root/", data["toDo"])]