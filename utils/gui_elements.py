import tkinter as tk
from tkinter import font
from utils.file_operations import set_file1_label, set_file2_label

def create_welcome_message(root):
    """
    Create a welcome message label in the GUI.

    Args:
        root: The Tkinter root window.
    """
    welcome_label = tk.Label(root, text="Welcome to the Cross-Referencing App!", font=("Arial", 16, "bold"), fg="blue")
    welcome_label.pack(pady=20)

def create_file_selection_widgets(root, get_file1_func, get_file2_func):
    """
    Create file selection buttons and labels in the GUI.

    Args:
        root: The Tkinter root window.
        get_file1_func: Function to get the path of the first file selected by the user.
        get_file2_func: Function to get the path of the second file selected by the user.

    Returns:
        tuple: Tuple containing file selection button frames, buttons, and labels.
    """

    file1_button_frame = tk.Frame(root)
    file1_button_frame.pack(pady=10)
    file1_button = tk.Button(file1_button_frame, text="Select File 1", font=("Arial", 12), command=lambda: set_file1_label(file1_path_label, get_file1_func(file1_path_label)))
    file1_button.pack(side=tk.LEFT, padx=5)
    file1_path_label = tk.Label(file1_button_frame, text="", font=("Arial", 12))
    file1_path_label.pack(side=tk.LEFT)

    file2_button_frame = tk.Frame(root)
    file2_button_frame.pack(pady=10)
    file2_button = tk.Button(file2_button_frame, text="Select File 2", font=("Arial", 12), command=lambda: set_file2_label(file2_path_label, get_file2_func(file2_path_label)))
    file2_button.pack(side=tk.LEFT, padx=5)
    file2_path_label = tk.Label(file2_button_frame, text="", font=("Arial", 12))
    file2_path_label.pack(side=tk.LEFT)

    return file1_button_frame, file1_button, file1_path_label, file2_button_frame, file2_button, file2_path_label

def create_column_entry(root):
    """
    Create an entry field to input the column name in the GUI.

    Args:
        root: The Tkinter root window.

    Returns:
        tk.Entry: The entry field widget.
    """
    column_label = tk.Label(root, text="Enter Column Name to Merge On:", font=("Arial", 12))
    column_label.pack(pady=10)
    column_entry = tk.Entry(root, font=("Arial", 12))
    column_entry.pack(pady=5)
    return column_entry

def create_merge_type_dropdown(root):
    """
    Create a dropdown menu to select the merge type in the GUI.

    Args:
        root: The Tkinter root window.

    Returns:
        tk.StringVar: The variable storing the selected merge type.
    """
    merge_type_label = tk.Label(root, text="Select Merge Type:", font=("Arial", 12))
    merge_type_label.pack(pady=10)

    merge_type_var = tk.StringVar()
    merge_type_var.set("inner")  # Default merge type

    merge_types = ["inner", "outer", "left", "right"]
    merge_type_dropdown = tk.OptionMenu(root, merge_type_var, *merge_types)
    merge_type_dropdown.config(font=("Arial", 12))
    merge_type_dropdown.pack(pady=5)
    return merge_type_var

def create_merge_button(root, merge_and_save):
    """
    Create a button to trigger the merge and save operation in the GUI.

    Args:
        root: The Tkinter root window.
        merge_and_save: Function to merge and save files.
    """
    merge_button = tk.Button(root, text="Merge and Save", font=("Arial", 14, "bold"), command=merge_and_save, bg="green", fg="white")
    merge_button.pack(pady=20)
