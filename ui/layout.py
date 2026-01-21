import tkinter as tk
from tkinter import ttk
from ui.styles import BG_COLOR, DISPLAY_BG, DISPLAY_TEXT, FONT_DISPLAY, configure_styles

class CalculatorUI:
    def __init__(self, root, on_click_callback):
        self.root = root
        self.on_click_callback = on_click_callback
        
        self.setup_window()
        self.create_display()
        self.create_buttons()
        self.create_history_area()

    def setup_window(self):
        self.root.title("Python Calculator")
        self.root.geometry("400x650")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)
        
        self.style = ttk.Style()
        configure_styles(self.style)

    def create_display(self):
        display_frame = tk.Frame(self.root, bg=BG_COLOR)
        display_frame.pack(expand=False, fill="both", padx=10, pady=20)

        self.display_var = tk.StringVar()
        
        self.display_entry = ttk.Entry(
            display_frame, 
            textvariable=self.display_var, 
            font=FONT_DISPLAY, 
            justify="right",
            style="Display.TEntry"
        )
        self.display_entry.pack(expand=True, fill="both", ipady=10) # ipady adds internal padding for height

    def create_buttons(self):
        buttons_frame = tk.Frame(self.root, bg=BG_COLOR)
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ('C', 0, 0, 'Clear.TButton'),  ('⌫', 0, 1, 'Clear.TButton'), ('/', 0, 2, 'Operator.TButton'), ('*', 0, 3, 'Operator.TButton'),
            ('7', 1, 0, 'Number.TButton'), ('8', 1, 1, 'Number.TButton'), ('9', 1, 2, 'Number.TButton'), ('-', 1, 3, 'Operator.TButton'),
            ('4', 2, 0, 'Number.TButton'), ('5', 2, 1, 'Number.TButton'), ('6', 2, 2, 'Number.TButton'), ('+', 2, 3, 'Operator.TButton'),
            ('1', 3, 0, 'Number.TButton'), ('2', 3, 1, 'Number.TButton'), ('3', 3, 2, 'Number.TButton'), ('=', 3, 3, 'Equal.TButton'),
            ('0', 4, 0, 'Number.TButton'), ('.', 4, 1, 'Number.TButton'), # Added decimal point for completeness
        ]
        
        layout_grid = [
            ('C', 0, 0, 'Clear.TButton', 1, 1), 
            ('⌫', 0, 1, 'Clear.TButton', 1, 1), 
            ('/', 0, 2, 'Operator.TButton', 1, 1), 
            ('*', 0, 3, 'Operator.TButton', 1, 1),
            
            ('7', 1, 0, 'Number.TButton', 1, 1), 
            ('8', 1, 1, 'Number.TButton', 1, 1), 
            ('9', 1, 2, 'Number.TButton', 1, 1), 
            ('-', 1, 3, 'Operator.TButton', 1, 1),
            
            ('4', 2, 0, 'Number.TButton', 1, 1), 
            ('5', 2, 1, 'Number.TButton', 1, 1), 
            ('6', 2, 2, 'Number.TButton', 1, 1), 
            ('+', 2, 3, 'Operator.TButton', 1, 1),
            
            ('1', 3, 0, 'Number.TButton', 1, 1), 
            ('2', 3, 1, 'Number.TButton', 1, 1), 
            ('3', 3, 2, 'Number.TButton', 1, 1), 
            ('=', 3, 3, 'Equal.TButton', 2, 1),
            
            ('0', 4, 0, 'Number.TButton', 1, 2),
            ('.', 4, 2, 'Number.TButton', 1, 1),
        ]

        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

        for (text, row, col, style, rowspan, colspan) in layout_grid:
            cmd = lambda t=text: self.on_click_callback(t)
            
            btn = ttk.Button(
                buttons_frame, 
                text=text, 
                command=cmd,
                style=style
            )
            btn.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew", padx=3, pady=3)

    def create_history_area(self):
        self.history_label = tk.Label(
            self.root, 
            text="History loaded.", 
            bg=BG_COLOR, 
            fg="white", 
            font=("Arial", 10)
        )
        self.history_label.pack(side="bottom", pady=5)

    def update_display(self, value):
        self.display_var.set(value)
        
    def get_display_text(self):
        return self.display_var.get()

    def update_history_label(self, text):
        self.history_label.config(text=text)
