import csv
import json
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to process CSV file and convert to JSON
def process_csv_to_json():

    sales_data = []
    try:
        # Prompt user to select CSV file
        filename = filedialog.askopenfilename(
            title="Select CSV File", 
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )
        if filename:
            # Read CSV file and clean up data
            with open(filename, newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cleaned_row = {key: value.strip('"') for key, value in row.items()}
                    sales_data.append(cleaned_row)
            # Save cleaned data to JSON file
            with open("transaction_data.json", "w") as jsonfile:
                json.dump(sales_data, jsonfile, indent=4)
            messagebox.showinfo("Success", "Data processed and saved to transaction_data.json")
    except Exception as e:
        # Display error message if an error occurs
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to open a supporting window
def open_supporting_window():
    def load_json_file():
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                data = json.load(file)
            # Clear any previous content
            text.delete('1.0', tk.END)
            # Display JSON data
            text.insert(tk.END, json.dumps(data, indent=4))

    supporting_window = tk.Toplevel(root)
    supporting_window.title("Supporting Window")
    supporting_window.geometry("400x300")
    supporting_window.configure(bg="#0066cc")

    label = tk.Label(supporting_window, text="Select a JSON file:", bg="#0066cc", fg="white")
    label.pack(pady=10)

    load_button = tk.Button(supporting_window, text="Load JSON File", command=load_json_file)
    load_button.pack(pady=5)

    text = tk.Text(supporting_window, wrap="word", width=40, height=15)
    text.pack(expand=True, fill="both", padx=10, pady=5)

    close_button = tk.Button(supporting_window, text="Close", command=supporting_window.destroy)
    close_button.pack(pady=5)

# GUI setup
root = tk.Tk()
root.title("Sales Data Processor - Wayne State University")
root.geometry("300x150")
root.configure(bg="#0066cc")

# Button to quit the application
quit_button = tk.Button(root, text="QUIT", command=root.quit, bg="#cc0000", fg="white")
quit_button.pack(pady=20)

# Button to trigger data processing from CSV to JSON
process_button = tk.Button(root, text="Process Data", command=process_csv_to_json, bg="#009933", fg="white")
process_button.pack(pady=10)

# Button to open a supporting window
supporting_window_button = tk.Button(root, text="Supporting Window", command=open_supporting_window, bg="#003399", fg="white")
supporting_window_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
