import pandas as pd
from tkinter import filedialog, messagebox

def merge_excel_files(file1_path, file2_path, column_name, merge_type='inner'):
    """
    Merge two Excel files based on the specified column and merge type.

    Args:
        file1_path (str): Path of the first Excel file.
        file2_path (str): Path of the second Excel file.
        column_name (str): Name of the column to merge on.
        merge_type (str): Type of merge operation (inner, outer, left, right). Default is 'inner'.

    Returns:
        pd.DataFrame: Merged DataFrame.
    """
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)

    merged_df = pd.merge(df1, df2, on=column_name, how=merge_type)

    return merged_df

def merge_csv_files(file1_path, file2_path, column_name, merge_type='inner'):
    """
    Merge two CSV files based on the specified column and merge type.

    Args:
        file1_path (str): Path of the first CSV file.
        file2_path (str): Path of the second CSV file.
        column_name (str): Name of the column to merge on.
        merge_type (str): Type of merge operation (inner, outer, left, right). Default is 'inner'.

    Returns:
        pd.DataFrame: Merged DataFrame.
    """
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    merged_df = pd.merge(df1, df2, on=column_name, how=merge_type)

    return merged_df

def save_to_csv(dataframe):
    """
    Save DataFrame as a CSV file.

    Args:
        dataframe (pd.DataFrame): DataFrame to save.
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    if file_path:
        dataframe.to_csv(file_path, index=False)
        messagebox.showinfo("Save Successful", f"The merged result has been saved as CSV to {file_path}")

def merge_and_save(file1_path, file2_path, column_name, merge_type):
    """
    Merge two files based on the specified column and merge type, then save the result as a CSV file.

    Args:
        file1_path (str): Path of the first file.
        file2_path (str): Path of the second file.
        column_name (str): Name of the column to merge on.
        merge_type (str): Type of merge operation (inner, outer, left, right).
    """
    try:
        if file1_path.endswith('.csv') and file2_path.endswith('.csv'):
            merged_df = merge_csv_files(file1_path, file2_path, column_name, merge_type)
        elif file1_path.endswith('.xlsx') and file2_path.endswith('.xlsx'):
            merged_df = merge_excel_files(file1_path, file2_path, column_name, merge_type)
        else:
            raise ValueError("File types must match (both Excel or both CSV)")

        save_to_csv(merged_df)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
