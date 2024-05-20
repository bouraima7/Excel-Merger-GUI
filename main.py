import tkinter as tk
from utils.gui_elements import *
from utils.merge_operations import merge_and_save
from utils.file_operations import get_file1, get_file2, set_file1_label, set_file2_label, get_file1_label, get_file2_label

def reset_gui():
    """
    Function to reset the GUI by clearing the selected file labels.
    """
    set_file1_label(file1_path_label, "")
    set_file2_label(file2_path_label, "")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Excel Merger")

    # Create GUI elements
    create_welcome_message(root)
    file1_button_frame, file1_button, file1_path_label, file2_button_frame, file2_button, file2_path_label = create_file_selection_widgets(root, get_file1, get_file2)
    column_entry = create_column_entry(root)
    merge_type_var = create_merge_type_dropdown(root)
    create_merge_button(root, lambda: merge_and_save(get_file1_label(file1_path_label), get_file2_label(file2_path_label), column_entry.get().strip(), merge_type_var.get()))
    reset_button = tk.Button(root, text="Reset", command=reset_gui)
    reset_button.pack(pady=10)

    root.mainloop()
