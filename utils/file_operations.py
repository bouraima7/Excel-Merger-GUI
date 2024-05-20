import tkinter as tk
from tkinter import filedialog

def get_file1_label(file1_path_label):
    """
    Function to get the label text for file 1.

    Args:
        file1_path_label (tk.Label): Label widget for file 1.

    Returns:
        str: Label text for file 1.
    """
    return file1_path_label.cget("text")

def get_file2_label(file2_path_label):
    """
    Function to get the label text for file 2.

    Args:
        file2_path_label (tk.Label): Label widget for file 2.

    Returns:
        str: Label text for file 2.
    """
    return file2_path_label.cget("text")

def set_file1_label(file1_path_label, path):
    """
    Function to set the label text for file 1.

    Args:
        file1_path_label (tk.Label): Label widget for file 1.
        path (str): Path of file 1.
    """
    file1_path_label.config(text=path)

def set_file2_label(file2_path_label, path):
    """
    Function to set the label text for file 2.

    Args:
        file2_path_label (tk.Label): Label widget for file 2.
        path (str): Path of file 2.
    """
    file2_path_label.config(text=path)

def get_file1(file1_path_label):
    """
    Function to get the path of the first file selected by the user.

    Args:
        file1_path_label (tk.Label): Label widget for file 1.

    Returns:
        str: Path of the first file.
    """
    path = filedialog.askopenfilename(filetypes=[("Excel/CSV files", "*.xlsx;*.csv")])
    if path:
        set_file1_label(file1_path_label, path)
    return path

def get_file2(file2_path_label):
    """
    Function to get the path of the second file selected by the user.

    Args:
        file2_path_label (tk.Label): Label widget for file 2.

    Returns:
        str: Path of the second file.
    """
    path = filedialog.askopenfilename(filetypes=[("Excel/CSV files", "*.xlsx;*.csv")])
    if path:
        set_file2_label(file2_path_label, path)
    return path
