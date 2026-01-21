"""
MEMBER 1: Main Application
This file acts as the bridge between UI, Logic, and Storage. 
It runs the main event loop.
"""
import tkinter as tk
from logic.calculator_logic import CalculatorLogic
from storage.history_manager import HistoryManager
from ui.layout import CalculatorUI

def main():
    root = tk.Tk()

    logic = CalculatorLogic()
    history_manager = HistoryManager()
    
    
    # State tracking
    state = {"should_reset": False}

    def on_button_click(char):
        current_text = ui.get_display_text()

        if char == 'C':
            ui.update_display("")
            state["should_reset"] = False
        
        elif char == '⌫':
            if state["should_reset"]:
                # If we just showed a result, backspace clears it (like C)
                ui.update_display("")
                state["should_reset"] = False
            else:
                # Remove last char
                new_text = current_text[:-1]
                ui.update_display(new_text)

        elif char == '=':
            if current_text:
                result = logic.evaluate(current_text)
                if "Error" not in result:
                    history_manager.save_entry(current_text, result)
                    update_history_preview()
                
                # Result is shown
                ui.update_display(result)
                # Enable the "smart reset" state
                state["should_reset"] = True
        
        else:
            # Handle standard inputs (Numbers and Operators)
            is_operator = char in ['+', '-', '*', '/']

            if state["should_reset"]:
                if is_operator:
                    ui.update_display(current_text + char)
                else:
                    ui.update_display(char)
                
                state["should_reset"] = False
            else:
                 if is_operator and current_text and current_text[-1] in ['+', '-', '*', '/']:
                     new_text = current_text[:-1] + char
                     ui.update_display(new_text)
                 else:
                     ui.update_display(current_text + char)

    ui = CalculatorUI(root, on_button_click)

    def update_history_preview():
        last_items = history_manager.load_history()
        if last_items:
            summary = "Recent: " + " | ".join([item.split('=')[1].strip() for item in last_items[-2:]])
            ui.update_history_label(summary)
        else:
            ui.update_history_label("History: Empty")

    update_history_preview()
    # Member 1: The Loop
    root.mainloop()

if __name__ == "__main__":
    main()
