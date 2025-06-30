import tkinter as tk
from functools import partial
from excel_paths import excel_files
from excel_utils import open_excel_file

def create_ui():
    # color design
    bg_color = "#F7EEDD"      
    button_color = "#A9DBDA"   
    hover_color = "#2D7685"    
    text_color = "#035968"     

    root = tk.Tk()
    root.title("🌊 Excel Opener - Oceanside")
    root.geometry("600x375")
    root.configure(bg=bg_color)

    # header
    tk.Label(
        root,
        text="🌊 Excel Opener · Oceanside",
        font=("Segoe UI", 16, "bold"),
        bg=bg_color,
        fg=text_color
    ).pack(pady=12)

    # main container frame
    main_frame = tk.Frame(root, bg=bg_color)
    main_frame.pack(pady=10)

    # left, center & right container frames
    left_frame = tk.Frame(main_frame, bg=bg_color)
    center_frame = tk.Frame(main_frame, bg=bg_color)
    right_frame = tk.Frame(main_frame, bg=bg_color)

    # separators
    separator1 = tk.Frame(main_frame, width=2, bg=text_color, height=280)
    separator2 = tk.Frame(main_frame, width=2, bg=text_color, height=280)

    left_frame.grid(row=0, column=0, padx=10)
    separator1.grid(row=0, column=1, padx=5, sticky="ns")
    center_frame.grid(row=0, column=2, padx=10)
    separator2.grid(row=0, column=3, padx=5, sticky="ns")
    right_frame.grid(row=0, column=4, padx=10)

    # btn feature
    def create_hover_button(parent, label, path):
        btn = tk.Button(
            parent,
            text=label,
            width=20,
            height=2,
            font=("Segoe UI", 10, "bold"),
            bg=button_color,
            fg=text_color,
            activebackground=hover_color,
            activeforeground="white",
            bd=0,
            relief="flat",
            command=partial(open_excel_file, path)
        )
        btn.pack(pady=5)

    # classify buttons by prefix
    for label, path in excel_files.items():
        if label.startswith("5."):
            create_hover_button(right_frame, label, path)
        elif label.startswith("1.") :
            create_hover_button(left_frame, label, path)
        else:
            create_hover_button(center_frame, label, path)

    root.mainloop()

