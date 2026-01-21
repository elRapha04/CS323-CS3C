import os

class HistoryManager:
    def __init__(self, filename="history.txt"):
        self.filename = filename

    def save_entry(self, equation, result):
        """Appends a new calculation to the history file."""
        try:
            with open(self.filename, "a") as f:
                f.write(f"{equation} = {result}\n")
        except Exception as e:
            print(f"Error saving history: {e}")

    def load_history(self):
        """Returns the last 5 lines of history as a list of strings."""
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
                # Return the last 5 lines, stripped of whitespace
                return [line.strip() for line in lines[-5:]]
        except Exception as e:
            print(f"Error loading history: {e}")
            return []

    def clear_history(self):
        """Clears the history file."""
        try:
            with open(self.filename, "w") as f:
                f.write("")
        except Exception as e:
            print(f"Error clearing history: {e}")
