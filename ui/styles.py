BG_COLOR = "#2C3E50"        # Dark Blueish Grey
DISPLAY_BG = "#ECF0F1"      # Light Grey
DISPLAY_TEXT = "#2C3E50"    # Dark Text
BTN_NUM_BG = "#34495E"      # Blue Grey
BTN_OP_BG = "#E67E22"       # Orange
BTN_EQ_BG = "#27AE60"       # Green
BTN_CLR_BG = "#C0392B"      # Red

# Fonts
FONT_DISPLAY = ("Arial", 24, "bold")


def configure_styles(style):
    """
    Configures ttk styles for the application.
    """
    style.theme_use('clam') # 'clam' usually allows easier color customization than 'vista'
    
    # Common Button Settings
    style.configure("TButton", font=("Arial", 14, "bold"), padding=10, relief="flat")
    
    # Number Buttons
    style.configure("Number.TButton", background=BTN_NUM_BG, foreground="white", borderwidth=0)
    style.map("Number.TButton", background=[('active', '#5D6D7E')]) # Lighter on hover

    # Operator Buttons
    style.configure("Operator.TButton", background=BTN_OP_BG, foreground="white", borderwidth=0)
    style.map("Operator.TButton", background=[('active', '#D35400')])

    # Equal Button
    style.configure("Equal.TButton", background=BTN_EQ_BG, foreground="white", borderwidth=0)
    style.map("Equal.TButton", background=[('active', '#1E8449')])

    # Clear/Backspace Buttons
    style.configure("Clear.TButton", background=BTN_CLR_BG, foreground="white", borderwidth=0)
    style.map("Clear.TButton", background=[('active', '#922B21')])

    # Display Entry Styling (Attempting a cleaner look)
    # ttk.Entry is harder to round without images/canvas, but we can make it flat and clean
    style.configure("Display.TEntry", 
        fieldbackground=DISPLAY_BG, 
        foreground=DISPLAY_TEXT, 
        borderwidth=5, 
        relief="flat",
        padding=10
    )
